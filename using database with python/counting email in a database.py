"""
To get credit for this assignment, perform the instructions below and upload your SQLite3 database here:
No file chosen
(Must have a .sqlite suffix)
Hint: The top organizational count is 536.
You do not need to export or convert the database - simply upload the .sqlite file that your program creates.
See the example code for the use of the connect() statement.

Counting Organizations
This application will read the mailbox data (mbox.txt) and count the number of email messages per organization
(i.e. domain name of the email address) using a database with the following schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)
When you have run the program on mbox.txt upload the resulting database file above for grading.
If you run the program multiple times in testing or with dfferent files, make sure to empty out the data
before each run.

You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.

The data file for this application is the same as in previous assignments: http://www.py4e.com/code3/mbox.txt.

Because the sample code is using an UPDATE statement and committing the results to the database as each record
is read in the loop, it might take as long as a few minutes to process all the data. The commit insists on
completely writing all the data to disk every time it is called.

The program can be speeded up greatly by moving the commit operation outside of the loop. In any database program,
there is a balance between the number of operations you execute between commits and the importance of not losing
the results of operations that have not yet been committed.
"""
import sqlite3

connection = sqlite3.connect("emaildb.sqlite")  # connect to database
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS Counts")  # if exist use this
cursor.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")  # otherwise create table

fname = input("Enter file name: ")
if len(fname) < 1:
    "break"  # input and open file
fhand = open(fname)

for lines in fhand:  # read into file
    if not lines.startswith("From "):
        continue
    pieces = lines.split()
    email = pieces[1]  # looking for email
    piece = email.split("@")
    domain = piece[1]  # looking for domain
    cursor.execute("SELECT count FROM Counts WHERE org = ?", (domain,))
    row = cursor.fetchone()

    # update into database
    if row is None:
        cursor.execute("INSERT INTO Counts (org, count) VALUES (?, 1)", (domain,))
    else:
        cursor.execute("UPDATE Counts SET count = count + 1 WHERE org = ?", (domain,))
connection.commit()

# looking for data in database
sqlstr = "SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10"

for row in cursor.execute(sqlstr):
    print(str(row[0]), row[1])  # display rows of database

cursor.close()