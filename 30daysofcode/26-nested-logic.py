## Day 26: Nested Logic
## https://www.hackerrank.com/challenges/30-nested-logic

day, month, year = map(int, raw_input().strip().split(' '))

returnDay, returnMonth, returnYear = map(int, raw_input().strip().split(' '))


resYear =  year - returnYear
resMonth =  month - returnMonth
resDay =  day - returnDay

if resYear > 0:
    print 10000
elif resYear == 0 and resMonth > 0:
    print 500 * resMonth
elif resYear == 0 and resMonth == 0 and resDay > 0:
    print (resDay * 15)
else:
    print 0

