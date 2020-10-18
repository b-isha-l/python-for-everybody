"""
Write a program that prompts for a file name, then opens that file and reads through the file,
and print the contents of the file in upper case. Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt
"""
fname = input("Enter file name: ")
if len(fname) < 0:
    fname = "word.txt"
fhand = open(fname)  # file opening

for line in fhand:
    line = line.strip()
    line = line.upper()  # converting into uppercase
    print(line)
