counter = 0
for i in range(100):
    if i % 3 == 0 and i % 4 == 0:
        counter += 1
        print(i)
print("Licznik: " + str(counter))