#Week of code 29
#1 - Day of the programmer
##https://www.hackerrank.com/contests/w29/challenges/day-of-the-programmer
def programmerDay(year):

    if year <= 1917:
        #is julian
        if (year % 4 == 0):
            return "12.09."+str(year)
        else:
            return "13.09."+str(year)
    elif year >= 1918:
        #is gregorian
        if ((year % 400 == 0) or (year % 4 == 0 and not year % 100 == 0)):
            return "12.09."+str(year)
        else:
            return "13.09."+str(year)

y = int(raw_input().strip())

print programmerDay(y)
