

def reverseWords1(words):
	i = 0
	limit = 0
	newarr = []
	for word in words:
		if word == ' ':
			if limit == 0:
				newarr.append(''.join(words[limit:i]))
			else:
				newarr.append(''.join(words[limit+1:i]))

			limit = i
		elif i == len(words) - 1:
			newarr.append(''.join(words[limit+1:len(words)]))
		i+=1

	arr = []
	x = 0
	for i in reversed(newarr):
		if x == len(newarr)-1:
			arr += list(i)
			#arr.append(list(i))
		else:
			arr += list(i) + [' ']
			#arr.append(list(i) + [' '])
		x+=1
	return arr

def reverseWords2(words):
	n = len(words)

	words = mirrorReverse(words, 0, n-1)

	wordStart = None
	for i in range(0, n - 1):
		if arr[i] == ' ':
			if wordStart != None:
				words = mirrorReverse(words, wordStart, i-1)
				wordStart = None
		elif i == n-1:
			if wordStart != None:
				words = mirrorReverse(words, wordStart, i)
		else:
			if wordStart == None:
				wordStart = i
	return words

def mirrorReverse(arr, start, end):
	tmp = None
	while start < end:
		tmp = arr[start]
		arr[start] = arr[end]
		arr[end] = tmp
		start += 1
		end -= 1
		
	return arr


arr = [
	'p',
	'e',
	'r',
	'f',
	'e',
	'c',
	't',
	' ',
	'm',
	'a',
	'k',
	'e',
	's',
	' ',
	'p',
	'r',
	'a',
	'c',
	't',
	'i',
	'c',
	'e' 
]

print reverseWords1(arr)

print reverseWords2(arr)


