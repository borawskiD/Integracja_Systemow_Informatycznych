import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re

from Home import Home

url = 'https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/pomorskie/gdynia/gdynia/gdynia?priceMax=600000&viewType=listing'

headers = {
    'authority': 'www.google.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

response = requests.get(url, headers=headers)

Offers = {}

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    ogloszenia = soup.find_all('article', class_='css-136g1q2 e88tro00')
    i = 1
    for ogloszenie in ogloszenia:
        header_elem = ogloszenie.find('p', class_='ev8qziy2')
        header = header_elem.text.strip() if header_elem else "Brak nagłówka"

        dd_elements = ogloszenie.find_all('dd')

        if len(dd_elements) >= 3:
            cena = dd_elements[2].text.strip()
            test_cena = dd_elements[1].text.split(" ")[0]
            cena_za_m2 = cena.split('/')[0].strip()
            number = re.findall(r'\d+', cena_za_m2)
            number = int(''.join(number))
            print(number)

        else:
            cena = "Brak danych"
            cena_za_m2 = "Brak danych"

        print("Nagłówek:", header)
        print("Cena:", cena)
        print(test_cena)
        print("Cena za m2:", cena_za_m2)
        print("------")
        Offers[i] = Home(header, test_cena, number)
        i = i + 1
else:
    print("Nie udało się pobrać strony:", response.status_code)

# zapis do slownika - test
for Offer in Offers:
    print(str(Offers.get(Offer).price) + " " + str(Offers.get(Offer).price_for_m2) + " " + str(Offers.get(Offer).header_name))

#zapis do csv

def saveToCSV(Offers, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["Numer", "Naglowek", "Cena", "Cena za m2", "Powierzchnia"]
        writer.writerow(field)
        i = 0
        for Offer in Offers:
            row = [i, Offers.get(Offer).header_name, Offers.get(Offer).price, Offers.get(Offer).price_for_m2, Offers.get(Offer).area]
            writer.writerow(row)
            i = i + 1

saveToCSV(Offers, filename="home.csv")