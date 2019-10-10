"""
Problem 1 - Paying Debt off in a Year

Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly
payment required by the credit card company each month.
The following variables contain values as described below:

balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months,
print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41
instead of
Remaining balance: 813.4141998135
So your program only prints out one thing: the remaining balance at the end of the year in the format:
Remaining balance: 4784.0

A summary of the required math is found below:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
month = 1

while month < 13:
    interest = balance*(annualInterestRate/12)
    balance = balance + interest
    payment = balance * monthlyPaymentRate
    balance = balance - payment

    print("Month: " + str(round(month, 2)) + ", Interest: " + str(round(interest, 2)) + ", Payment: " + str(round(payment, 2)) + ", Balance: " + str(round(balance, 2)))
    month += 1

print("Remaining Balance: " + str(round(balance, 2)))
