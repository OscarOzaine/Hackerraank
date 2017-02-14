#Day 2: Operators
#https://www.hackerrank.com/challenges/30-operators

mealCost = float(raw_input().strip())
tip = float(raw_input().strip())
tax = float(raw_input().strip())

tip = mealCost * (tip / 100)
tax = mealCost * (tax / 100)

totalCost = int(round(mealCost + tip + tax, 0))

print "The total meal cost is " + str(totalCost) + " dollars."
