def countWays(n):
	global counts
	
	if n < 0:
		return 0
	elif n == 0:
		return 1
	else:
		counts += 1
		return countWays(n - 1) + countWays(n - 2) + countWays(n - 3)

def countWaysCache(n):
	cache = {}
	return _countWaysCache(n, cache)

def _countWaysCache(n, cache):
	global counts
	
	if n < 0:
		return 0
	elif n == 0:
		return 1
	else:

		if not cache.get(n):
			counts += 1
			cache[n] = _countWaysCache(n - 1, cache) + _countWaysCache(n - 2, cache) + _countWaysCache(n - 3, cache)

		return cache[n]


n = int(raw_input().strip())
counts = 0

## Brute Force Solution
print 'result = ' + str(countWays(n))
print 'computations = ' + str(counts)
print 

counts = 0

## Cache Solution (Memoization)
print 'result = ' + str(countWaysCache(n))
print 'computations = ' + str(counts)
print 


