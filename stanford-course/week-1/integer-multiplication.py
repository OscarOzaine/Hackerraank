
import sys

def multiplication_karatsuba(x, y):

	if x < 10 or y < 10:
		return x * y
	
	n = max(len(str(x)), len(str(y)))
	nby2 = n / 2
	
	a = x / 10**(nby2)
	b = x % 10**(nby2)
	c = y / 10**(nby2)
	d = y % 10**(nby2)
	
	ac = multiplication_karatsuba(a, c)
	bd = multiplication_karatsuba(b, d)
	# gauss trick
	ad_plus_bc = multiplication_karatsuba(a + b, c + d) - ac - bd

	# n as 2*nby2 takes care of both even and odd n
	prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd

	return prod

x, y = map(int, raw_input().strip().split(' '))

print x * y

print multiplication_karatsuba(x, y)

