balance = 999999
annualInterestRate = 0.18


def calc1(loan, interest, payment):
    unpaidBalance = loan
    for month in range(1, 13):
        unpaidBalance -= payment
        unpaidBalance = unpaidBalance + unpaidBalance * (interest / 12)
    return round(unpaidBalance, 2)


outstanding = balance
lowerBound = balance / 12
upperBound = (balance + balance * annualInterestRate) / 12

while abs(outstanding) > 0:
    minPay = (upperBound + lowerBound) / 2
    outstanding = calc1(balance, annualInterestRate, minPay)
    if outstanding > 0:
        lowerBound = minPay
    else:
        upperBound = minPay

print("Lowest Payment: " + str(round(minPay, 2)))
