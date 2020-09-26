"""
 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range,
 print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
 Score Grade
 >= 0.9 A
 >= 0.8 B
 >= 0.7 C
 >= 0.6 D
 < 0.6 F
 If the user enters a value out of range, print a suitable error message and exit.
"""
score = input('Enter a score: ')
score = float(score)

# checking if the score is out of range
if (score >= 1.0) or (score <= 0.0):
    print('Your score is out of range' +
          '\nscore must be between 0 and 1')
    exit()

# score is in range and testing each conditions
if score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
elif score < 0.6:
    print('F')
