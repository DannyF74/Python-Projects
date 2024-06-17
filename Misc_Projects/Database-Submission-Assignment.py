import sqlite3

# Below we are connecting to the test.db database and creating a new table
# called tbl_assignment. We have created two columns called ID (which is
# the primary key) and File_name which will hold the names of our files.
conn = sqlite3.connect('test.db')

with conn:   
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_assignment( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                File_name text)")
    conn.commit()
conn.close



# Here we are creating the tuple of file names called fileList. We then create
# a for loop which checks each item in the tuple. If the item ends with .txt, 
# the connection is created with the database, the item is split into a
# one element touple and inserted under the File_name column in the tbl_assignment table.

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg', 'World.txt','data.pdf','myPhoto.jpg')

for item in fileList:
    if item.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_assignment (File_name) VALUES (?)", (item,))
            print(item)
conn.close




