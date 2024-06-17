import os
import time

PATH = 'C:/A/'
files = []

# Loop to go through all files in a path and add every file that ends with
# .txt to the files list created above.
for file in os.listdir(PATH):
    if file.endswith('.txt'):
        files.append(os.path.join(PATH, file))

# For each result in the files list, the timeMod variable will find the modified
# time for the file in float format. The modStamp variable will take the float
# and convert it to a timestamp. We will then print that item in the list
# followed by a string to seporate them followed by its timestamp as a string
for i in files:
    timeMod = os.path.getmtime(i)
    modStamp = time.ctime(timeMod)
    print(i + " - " + str(modStamp))
