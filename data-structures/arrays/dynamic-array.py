#!/bin/python
#Dynamic Array
#Hackerrank.com
import sys

input_array = map(int, raw_input().strip().split(' '))

n = input_array[0]
q = input_array[1]

querys = []
for i in range(0, input_array[1]):
    input_array = map(int, raw_input().strip().split(' '))
    querys.append(input_array)

seqList = list()
for seq in range(0, n):
    seqList.append([])
    
lastAns = 0
for query in querys:
    if query[0] == 1:
        seq = seqList[(query[1] ^ lastAns) % n]
        seq.append(query[2])
    elif query[0] == 2:
        seq = seqList[(query[1] ^ lastAns) % n]
        lastAns = seq[query[2] % len(seq)]
        print lastAns
