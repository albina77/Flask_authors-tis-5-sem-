import sqlite3



with sqlite3.connect('database.db') as con:
    with open('schema.sql') as f:
        con.executescript(f.read())

    cur = con.cursor()

    cur.execute("INSERT INTO Persons VALUES (1, 'Алексеев Михаил Николаевич', '29.11.1918', '19.05.2007')",
                )
    cur.execute("INSERT INTO Countries VALUES (1, 'СССР')")
    cur.execute("INSERT INTO Types VALUES (1, 'Литература')")
    cur.execute("INSERT INTO Countries VALUES (2, 'Россия')")
    cur.execute("INSERT INTO Works VALUES (1, 'Дивизионка', 1969, 1)")
    cur.execute("INSERT INTO CountriesPersons VALUES (1, 2)",
                )
    cur.execute("INSERT INTO CountriesPersons VALUES (1, 1)")
    cur.execute("INSERT INTO PersonsWorks VALUES (1, 1)")
    cur.execute("INSERT INTO Persons VALUES (2, 'Стивен Спилберг', '18.12.1946', NULL)")
    cur.execute("INSERT INTO Countries VALUES (3, 'USA')")
    cur.execute("INSERT INTO Types VALUES (2, 'Films')")
    cur.execute("INSERT INTO CountriesPersons VALUES (2, 3)")
    cur.execute("INSERT INTO Works VALUES (2, 'Chelusti', 1975, 2)")
    cur.execute("INSERT INTO PersonsWorks VALUES (2, 2)")


    con.commit()
