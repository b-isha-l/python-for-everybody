"""
Write a program that prompts for a file name, then opens that file and reads
through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and
compute the average of those values and produce an output as shown below. Do not use
the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
when you are testing below enter mbox-short.txt as the file name.
"""

fname = input("Enter the file name: ")
if len(fname) < 0:
    fname = "mbox-short.txt"
fhand = open(fname)  # opening file

count = 0
sum_data = 0.0

for lines in fhand:  # reading file
    if not lines.startswith("X-DSPAM-Confidence:"):  # finding line
        continue
    lines = lines.strip()
    count += 1
    position = lines.find(":")  # finding number
    number = lines[position + 1:]
    number = float(number)  # converting into floating point
    sum_data += number

print("Average spam confidence: ", sum_data/count)  # finding and displaying average