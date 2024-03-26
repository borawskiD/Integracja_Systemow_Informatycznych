from faker import Faker
import sqlite3
import random

fake = Faker('pl_PL')

conn = sqlite3.connect('uczelnia.db')
c = conn.cursor()


c.execute("INSERT INTO Uczelnia (Nazwa, Patron, TypUczelni, IdUczelni) VALUES (?, ?, ?, ?)",
          (fake.company(), fake.name(), "Uniwersytet", 1))

for i in range(2):
    c.execute("INSERT INTO Wydzial (Nazwa, Budynek, IdWydzialu, IdUczelni) VALUES (?, ?, ?, ?)",
              (fake.company_suffix(), fake.street_name(), i + 1, 1))

for i in range(5):
    c.execute("INSERT INTO Wykladowca (Imie, Nazwisko, StopienNaukowy, IdWykladowcy) VALUES (?, ?, ?, ?)",
              (fake.first_name(), fake.last_name(), fake.job(), i + 1))

for i in range(5):
    c.execute("INSERT INTO Przedmiot (Nazwa, ECTS, TypPrzedmiotu, IdPrzedmiotu) VALUES (?, ?, ?, ?)",
              (fake.word(), random.randint(2, 6), fake.job(), i + 1))

for i in range(2):
    c.execute("INSERT INTO Grupa_studencka (Nazwa, Kierunek, DataStartu, IdGrupy, IdWydzialu) VALUES (?, ?, ?, ?, ?)",
              (fake.random_element(elements=('1A', '1B', '2A', '2B', '3A')), fake.job(), fake.date_this_decade(), i + 1,
               i + 1))

for i in range(1, 7):
    c.execute("INSERT INTO Student (Imie, Nazwisko, NumerAlbumu, IdGrupy) VALUES (?, ?, ?, ?)",
              (fake.first_name(), fake.last_name(), i, random.randint(1, 2)))

for student_id in range(1, 7):
    for przedmiot_id in range(1, 6):
        c.execute(
            "INSERT INTO Ocena (Wartosc, Data, CzyPoprawa, IdOceny, IdPrzedmiotu, NumerAlbumu) VALUES (?, ?, ?, ?, ?, ?)",
            (random.randint(2, 5), fake.date_this_decade(), random.randint(0, 1),
             student_id * przedmiot_id * random.randint(1, 100), przedmiot_id, student_id))

conn.commit()
conn.close()
