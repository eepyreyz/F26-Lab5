# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2026/11/2
# Purpose: Write data to a file.
# Usage: ./lab5b.py

# TODO 1: Paste the code provided in readme.md file.
f = open('fruits.txt', 'w')
f.write('1. Apples are crunchy.\n2. Oranges are sweet, sour and juicy.\n3. Strawberries are sweet.\n4. Which fruit do you like?')
f.close()
print("file fruits.txt has been created")


# TODO 3: Validate that the new file was created.

print("Reading the file fruits.txt ...")

# TODO 4: Using a while loop and the readline() function, 
        # print each line of fruits.txt
f = open('fruits.txt', 'r') #open it again in read mode
line = f.readline()

while line != "":
    print(line.strip("\n"))
    line = f.readline()

