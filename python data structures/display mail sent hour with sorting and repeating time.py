"""
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for
each of the messages. You can pull the hour out from the 'From ' line by finding the time and then
splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

fname = input("Enter file name:")
if len(fname) < 0:
    fname = "mbox-short.txt"
fhand = open(fname)
time = list()
count = dict()

for lines in fhand:
    if not lines.startswith("From") or lines.startswith("From:"):
        continue
    line = lines.split()
    date = line[5]
    hrs = date.split(":")
    time.append(hrs[0])
time.sort()
for t in time:
    count[t] = count.get(t, 0) + 1
for key, value in count.items():
    print(key, value)
