"""
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number
of mail messages. The program looks for 'From ' lines and takes the second word of those lines as
the person who sent the mail. The program creates a Python dictionary that maps the sender's mail
address to a count of the number of times they appear in the file. After the dictionary is produced,
the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

fname = input("Enter file name: ")
if len(fname) < 0:
    fname = "mbox-short.txt"
sent_lst = dict()
fhand = open(fname)

for lines in fhand:
    if not lines.startswith("From"):
        continue
    line = lines.split()
    email = line[1]
    sent_lst[email] = sent_lst.get(email, 0) + 1

large = None
max = None
for key in sent_lst:
    if large is None:
        large = sent_lst[key]
    if large < sent_lst[key]:
        large = sent_lst[key]
        max = key
print(max, int(large/2))