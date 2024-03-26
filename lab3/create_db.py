import sqlite3

conn = sqlite3.connect('uczelnia.db')
c = conn.cursor()

tables = [
    """CREATE TABLE IF NOT EXISTS Uczelnia (
        Nazwa VARCHAR(200) NOT NULL,
        Patron VARCHAR(150) NOT NULL,
        TypUczelni VARCHAR(60) NOT NULL,
        IdUczelni INT NOT NULL PRIMARY KEY
    );""",
    """CREATE TABLE IF NOT EXISTS Wydzial (
        Nazwa VARCHAR(100) NOT NULL,
        Budynek VARCHAR(50) NOT NULL,
        IdWydzialu INT NOT NULL PRIMARY KEY,
        IdUczelni INT NOT NULL,
        FOREIGN KEY (IdUczelni) REFERENCES Uczelnia(IdUczelni)
    );""",
    """CREATE TABLE IF NOT EXISTS Grupa_studencka (
        Nazwa VARCHAR(40) NOT NULL,
        Kierunek VARCHAR(60) NOT NULL,
        DataStartu DATE NOT NULL,
        IdGrupy INT NOT NULL PRIMARY KEY,
        IdWydzialu INT NOT NULL,
        FOREIGN KEY (IdWydzialu) REFERENCES Wydzial(IdWydzialu)
    );""",
    """CREATE TABLE IF NOT EXISTS Wykladowca (
        Imie VARCHAR(40) NOT NULL,
        Nazwisko VARCHAR(70) NOT NULL,
        StopienNaukowy VARCHAR(60) NOT NULL,
        IdWykladowcy INT NOT NULL PRIMARY KEY
    );""",
    """CREATE TABLE IF NOT EXISTS Przedmiot (
        Nazwa VARCHAR(50) NOT NULL,
        ECTS INT NOT NULL,
        TypPrzedmiotu VARCHAR(40) NOT NULL,
        IdPrzedmiotu INT NOT NULL PRIMARY KEY
    );""",
    """CREATE TABLE IF NOT EXISTS Student (
        Imie VARCHAR(40) NOT NULL,
        Nazwisko VARCHAR(50) NOT NULL,
        NumerAlbumu INT NOT NULL PRIMARY KEY,
        IdGrupy INT NOT NULL,
        FOREIGN KEY (IdGrupy) REFERENCES Grupa_studencka(IdGrupy)
    );""",
    """CREATE TABLE IF NOT EXISTS Ocena (
        Wartosc INT NOT NULL,
        Data DATE NOT NULL,
        CzyPoprawa INT NOT NULL,
        IdOceny INT NOT NULL PRIMARY KEY,
        IdPrzedmiotu INT NOT NULL,
        NumerAlbumu INT NOT NULL,
        FOREIGN KEY (IdPrzedmiotu) REFERENCES Przedmiot(IdPrzedmiotu),
        FOREIGN KEY (NumerAlbumu) REFERENCES Student(NumerAlbumu)
    );""",
    """CREATE TABLE IF NOT EXISTS Pracuje (
        IdWykladowcy INT NOT NULL,
        IdWydzialu INT NOT NULL,
        PRIMARY KEY (IdWykladowcy, IdWydzialu),
        FOREIGN KEY (IdWykladowcy) REFERENCES Wykladowca(IdWykladowcy),
        FOREIGN KEY (IdWydzialu) REFERENCES Wydzial(IdWydzialu)
    );""",
    """CREATE TABLE IF NOT EXISTS Prowadzi (
        IdWykladowcy INT NOT NULL,
        IdPrzedmiotu INT NOT NULL,
        PRIMARY KEY (IdWykladowcy, IdPrzedmiotu),
        FOREIGN KEY (IdWykladowcy) REFERENCES Wykladowca(IdWykladowcy),
        FOREIGN KEY (IdPrzedmiotu) REFERENCES Przedmiot(IdPrzedmiotu)
    );""",
    """CREATE TABLE IF NOT EXISTS Uczestniczy (
        NumerAlbumu INT NOT NULL,
        IdPrzedmiotu INT NOT NULL,
        PRIMARY KEY (NumerAlbumu, IdPrzedmiotu),
        FOREIGN KEY (NumerAlbumu) REFERENCES Student(NumerAlbumu),
        FOREIGN KEY (IdPrzedmiotu) REFERENCES Przedmiot(IdPrzedmiotu)
    );"""
]

for table in tables:
    c.execute(table)

conn.commit()
conn.close()

