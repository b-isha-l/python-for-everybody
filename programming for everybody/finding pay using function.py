"""
 Write a program to prompt the user for hours and rate per hour using input to compute
 gross pay. Pay should be the normal rate for hours up to 40 and time-and-a-half for the
 hourly rate for all hours worked above 40 hours. Put the logic to do the computation of
 pay in a function called computepay() and use the function to do the computation. The
 function should return a value. Use 45 hours and a rate of 10.50 per hour to test the
 program (the pay should be 498.75). You should use input to read a string and float() to
 convert the string to a number.
"""
hrs = input('Enter hours: ')
rate = input('Enter rate: ')


# function to compute pay
def computepay(hr, rate):
    if hr > 40:
        pay1 = 40 * rate
        pay2 = (hr - 40) * rate * 1.5
        allpay = pay1 + pay2
    else:
        allpay = hr * rate
    return allpay


# function calling
pay = computepay(float(hrs), float(rate))
print("Pay", pay)