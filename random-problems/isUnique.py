
# Solving with a hashmap
def isUnique(words):
	hashmap = {}
	for s in words:
		if s in hashmap:
			return False
		else:
			hashmap[s] = 1
			
	return True

# Solving with a set
def isUnique2(words):
	sett = set()
	for s in words:
		if s in sett:
			return False
		sett.add(s)
	return True

# Measuring the length of the string with the length of the same string as a set
def isUnique3(words):
	if (len(set(words)) == len(words)):
		return True
	return False


words = 'abcd'

print(isUnique(words))

print(isUnique2(words))

print(isUnique3(words))

