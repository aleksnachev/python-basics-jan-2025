#сума = депозирана сума + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
#1. Депозирана сума – реално число в интервала [100.00 … 10000.00]
#2. Срок на депозита (в месеци) – цяло число в интервала [1…12]
#3. Годишен лихвен процент – реално число в интервала [0.00 …100.00]


deposit_amount = float(input())
deposit_months = int(input())
annual_interest_rate = float(input())

total = deposit_amount+deposit_months*((deposit_amount*annual_interest_rate/100)/12)
print(total)