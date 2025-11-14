principal = 1000
rate = 0.07
years = [10, 20, 30]

for n in years:
    amount = principal * (1 + rate) ** n
    print("After", n, "years, you will have: $", amount)
