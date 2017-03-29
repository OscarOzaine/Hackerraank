'''
Note: Write a solution with O(n2) time complexity, since this is what you would be asked to do during a real interview.

You have an array a composed of exactly n elements. Given a number x, determine whether or not a contains three elements for which the sum is exactly x.
'''

def tripletSum(x, a):
	a = sorted(a, reverse=False)
	
	for i in range(0, len(a) - 2):
		
		index_f = i + 1
		index_l = len(a) - 1

		while index_f < index_l:
			s = a[i] + a[index_f]
			s = s + a[index_l]
			if s == x:
				return True
			elif s < x:
				index_f += 1
			else:
				index_l -= 1

	return False
	
x = int(raw_input().strip())

array = map(int, raw_input().strip().split(' '))

print tripletSum(x, array)
