##Mars Exploration
##https://www.hackerrank.com/challenges/mars-exploration

string = raw_input().strip()

count = 0
word = 'SOS'
x = 0
for s in string:
    if (s != word[x]):
        count += 1
    x += 1
    x = x % 3

print count
