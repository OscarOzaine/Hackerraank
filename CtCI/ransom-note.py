#Hash Tables: Ransom note

from collections import Counter

def ransom_note(magazine, ransom):
    for i in ransom:
        if ransom[i] > magazine[i]:
            return 0
    return 1
    
m, n = map(int, raw_input().strip().split(' '))
magazine = Counter(raw_input().strip().split(' '))
ransom = Counter(raw_input().strip().split(' '))

answer = ransom_note(magazine, ransom)

if answer:
    print "Yes"
else:
    print "No"
    