# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Rey Abbas
# Date: 2026/11/2
# Purpose: Process File data.
# Usage: ./lab5d.py

# TODO 1: Create pathing variables for your pythonStatements.txt and machineCode.txt files
machine = open('machineCode.txt', 'r')
python = open('pythonStatements.txt', 'r')
output = open('output.txt','w')
# TODO 2: Strip all leading and trailing spaces, as well as comments from pythonStatements.txt
# TODO 3: Write the pure python statement with its corresponding machine code statement in a new file called "output.txt"
# TODO 4: Make sure you add a tab between the python statement and its corresponding machine code when writing in output.txt

machine_line = machine.readline()
python_line = python.readline()

while python_line != "" and machine_line!="":
    lst = python_line.split("#")
    python_line = lst[0].strip() #jst the line without the comment

    machine_line = machine_line.strip()

    output.write(python_line + "\t" + machine_line + "\n")

    #read next line
    machine_line = machine.readline()
    python_line = python.readline()

python.close()
machine.close()
output.close()
