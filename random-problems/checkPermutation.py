
def checkPermutation2(str1, str2):
	if ((len(str1) == len(str2)) and (str(''.join(reversed(str1))) == str2) ):
		return True

	return False


def reverseString(str1):
	str2 = ""
	for i in str1:
		str2 = i + str2

	return str2

def checkPermutation(str1, str2):
	if (len(str1) == len(str2)):
		if (reverseString(str1) == str2):
			return True

	return False


str1 = 'abc'
str2 = 'cba'

print(checkPermutation(str1, str2))

print(checkPermutation2(str1, str2))
