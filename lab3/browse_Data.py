import sqlite3

conn = sqlite3.connect('uczelnia.db')
c = conn.cursor()

print("Wszyscy studenci:")
c.execute("SELECT * FROM Student")
students = c.fetchall()
for student in students:
    print(student)

print("\nWszyscy studenci 1 grupy:")
c.execute("SELECT * FROM Student WHERE IdGrupy = 1")
group_1_students = c.fetchall()
for student in group_1_students:
    print(student)

print("\nStudenci, którzy z jednego przedmiotu otrzymali ocenę wyższą bądź równą 4:")
c.execute("SELECT DISTINCT Student.* FROM Student INNER JOIN Ocena ON Student.NumerAlbumu = Ocena.NumerAlbumu WHERE Ocena.Wartosc >= 4")
students_high_grades = c.fetchall()
for student in students_high_grades:
    print(student)

print("\nWszyscy wykładowcy z prowadzonymi przez nich przedmiotami:")
c.execute("SELECT DISTINCT Wykladowca.* FROM Wykladowca INNER JOIN Prowadzi ON Wykladowca.IdWykladowcy = Prowadzi.IdWykladowcy")
lecturers_with_subjects = c.fetchall()
for lecturer in lecturers_with_subjects:
    print(lecturer)

print("\nWydział z wszystkimi grupami studenckimi:")
c.execute("SELECT Wydzial.Nazwa, Grupa_studencka.* FROM Wydzial INNER JOIN Grupa_studencka ON Wydzial.IdWydzialu = Grupa_studencka.IdWydzialu")
departments_with_groups = c.fetchall()
for department in departments_with_groups:
    print(department)

print("\nWszyscy studenci wraz z ich średnią arytmetyczną ocen:")
c.execute("SELECT Student.*, AVG(Ocena.Wartosc) AS Srednia FROM Student INNER JOIN Ocena ON Student.NumerAlbumu = Ocena.NumerAlbumu GROUP BY Student.NumerAlbumu")
students_with_average_grade = c.fetchall()
for student in students_with_average_grade:
    print(student)

conn.close()