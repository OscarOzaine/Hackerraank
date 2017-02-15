#Bigger is Greater
##https://www.hackerrank.com/challenges/bigger-is-greater

def lexicographically_next_permutation(array):
    #Generates the lexicographically next permutation.
    array = [ord(numeric_string) for numeric_string in array]
    
    i = len(array) - 2
    while not (i < 0 or array[i] < array[i + 1]):
        i -= 1
        
    if i < 0:
        return False
    
    j = len(array) - 1
    while not (array[j] > array[i]):
        j -= 1
    #swap
    array[i], array[j] = array[j], array[i]
    # reverse elements from position i+1 till the end of the sequence
    array[i+1:] = reversed(array[i+1:])
    
    result = [chr(numeric_string) for numeric_string in array]
    
    return ''.join(result)
	
n = raw_input().strip()
read = ''

for i in range(0, int(n)):
	read = raw_input().strip()
	result = lexicographically_next_permutation(read)
	if result == False:
		print 'no answer'
	else:
		print result
	
