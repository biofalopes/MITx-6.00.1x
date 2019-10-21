balance = 812
annualInterestRate = 0.18
minPay = 10


def calc1(balance, annualInterestRate, minPay):
    unpaidBalance = balance
    for month in range(1, 13):
        unpaidBalance -= minPay
        unpaidBalance = unpaidBalance + unpaidBalance * (annualInterestRate / 12)
    return unpaidBalance


while calc1(balance, annualInterestRate, minPay) >= 0:
    minPay += 10

print("Lowest Payment: " + str(round(minPay, 2)))
