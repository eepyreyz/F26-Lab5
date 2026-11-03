# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2026/11/2
# Purpose: Process File data.
# Usage: ./lab5c.py

# TO DO 1: Run the code provided in readme.md file.
with open("rhyme.txt", "w") as dataFile :
  dataFile.write("I made myself a snowball\nAs perfect as could be.\nI thought I'd keep it as a pet\nAnd let it sleep with me.")

# TO DO 2: Open rhyme.txt file.
file = open('rhyme.txt',"r")
line = file.readline()

# TO DO 3: Print the output as directed in readme.md file.
while line != "":
    line = line.strip()
    line = line.strip(".")
    words_list = line.split()
    word_count = len(words_list)

    print(f"{line} --- {word_count} words")

    line = file.readline() #updates the fileline we r reading to the next line

file.close()