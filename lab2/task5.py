from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Open the URL with the custom SSL context
data = urlopen('https://www.amw.gdynia.pl', context=ssl_context).read()

soup = BeautifulSoup(data, 'html.parser')

links = soup.find_all('a')

with open('linki.txt', 'w') as f:
    for link in links:
        href = link.get('href')
        if href:
            print(href)
            f.write(href)
            f.write("\n")

