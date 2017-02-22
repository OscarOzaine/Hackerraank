##Big Sorting
##https://www.hackerrank.com/contests/w29/challenges/big-sorting

import sys

n = int(raw_input().strip())

unsorted = []
unsorted_i = 0
for unsorted_i in xrange(n):
    unsorted_t = str(raw_input().strip())
    unsorted.append(int(unsorted_t))
    
    
def mergesort( aList ):
    _mergesort( aList, 0, len( aList ) - 1 )
    return aList
 
def _mergesort( aList, first, last ):
	# break problem into smaller structurally identical pieces
	mid = ( first + last ) / 2
	if first < last:
		_mergesort( aList, first, mid )
		_mergesort( aList, mid + 1, last )

	# merge solved pieces to get solution to original problem
	a, f, l = 0, first, mid + 1
	tmp = [None] * ( last - first + 1 )
 
	while f <= mid and l <= last:
		if aList[f] < aList[l]:
			tmp[a] = aList[f]
			f += 1
		else:
			tmp[a] = aList[l]
			l += 1
		a += 1

	if f <= mid:
		tmp[a:] = aList[f:mid + 1]

	if l <= last:
		tmp[a:] = aList[l:last + 1]

	a = 0
	while first <= last:
		aList[first] = tmp[a]
		first += 1
		a += 1

sorted = mergesort(unsorted)

for i in sorted:
    print i
