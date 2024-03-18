import random

num = random.randint(1, 100)
i = 0
counter = 0
while int(i) != num:
    i = input("Podaj liczbe pomiedzy 1 a 100:")
    if int(i) > num:
        print("Za duzo!")
    if int(i) < num:
        print("Za malo!")
    counter += 1

print("Gratulacje! Wylosowana liczba to: " + i + " prob: " + str(counter))
