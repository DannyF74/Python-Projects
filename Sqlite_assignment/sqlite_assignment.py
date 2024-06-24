import sqlite3
connection = sqlite3.connect("test_database.db")

c = connection.cursor()

c.execute("CREATE TABLE people(FirstName TEXT, LastName TEXT, Age INT)")

