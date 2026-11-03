# Add comments before you do anything else.
#!/usr/bin/env python3
# Author: Rey Abbasd
# Date: 2026/11/2
# Purpose: Read a text file.
# Usage: ./lab5a.py

# TODO 1: Create a file called data2.txt, and paste the contents found in README.md
#Done

# TODO 2: Complete the functions below.

def read_file_lineByLine(file_name):
    # Takes file_name as a string, reads the file in a loop one line at a time and prints each line.
    with open(file_name, "r") as file:
        for line in file:
            print(line.strip("\n"))


def read_file_list(file_name):
    # Takes a file_name as string, read file line by line and add the line in a list as a list element without new-line characters
    # Return the list.
    list_element = []
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip("\n\t")
            list_element.append(line)
    return(list_element)

def main():
    file_name = 'data2.txt'
    read_file_lineByLine(file_name)
    print(read_file_list(file_name))

 # TODO 3: Run the script and confirm output.
if __name__ == "__main__":
    main()