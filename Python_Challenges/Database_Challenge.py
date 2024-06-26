import sqlite3

# Creating a new database stored in RAM
conn = sqlite3.connect(':memory:')

# Creating a variable to act as the cursor for the database
c = conn.cursor()

# Creating a new table called tbl_people and setting up the columns.
# ID column will auto increment.
c.execute("""CREATE TABLE IF NOT EXISTS tbl_people (
          ID INTEGER PRIMARY KEY,
          Name TEXT,
          Species TEXT,
          IQ TEXT
          )""")

# Setting up a tuple with all our values
PeopleValues = (("Jean-Baptiste Zorg", "Human", "122"),("Korben Dallas", "Meat Popsicle", "100"),("Ak'not","Mangalore","5"))

# Executing an insert query multiple times for each item in the tuple using c.executemany.
# Then printing the results to check all data has been inserted correctly
c.executemany("INSERT INTO tbl_people (Name,Species,IQ) VALUES (?,?,?)", PeopleValues)
c.execute("SELECT * FROM tbl_people")
records = c.fetchall()
for row in records:
    print(row)

# Executing an update query to change the species of Korben Dallas to Human.
# Then checking the updated values of everything to make sure only what
# we have asked to be changed has been changed.
c.execute("UPDATE tbl_people SET Species = 'Human' WHERE Name = 'Korben Dallas'")
c.execute("SELECT * FROM tbl_people")
update_record = c.fetchall()
for row in update_record:
    print(row)

# Selecting only the Name and IQ Columns for the rows where species is set to Human.
c.execute("SELECT Name,IQ FROM tbl_people WHERE Species = 'Human'")
humans = c.fetchall()
for row in humans:
    print(row)

# Committing the queries and closing the connection.
conn.commit()
conn.close()
