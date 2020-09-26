"""
Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters
anything other than a valid number catch it with a try/except and put out an appropriate message
and ignore the number.
"""
# First assign smallest and largest as None
Largest = None
Smallest = None

while True:
    user_in = input('Enter your input: ')

    if user_in == 'done':
        break  # if user enter done then stop

    # checking for invalid input and ignoring using try/except
    try:
        num = int(user_in)

        # finding largest number
        if Largest is None:
            Largest = num
        elif Largest < num:
            Largest = num

        # finding smallest number
        if Smallest is None:
            Smallest = num
        elif Smallest > num:
            Smallest = num

    except:
        print('Invalid input!')
        continue
print("Maximum is", Largest)
print("Minimum is", Smallest)
