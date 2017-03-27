def checkPalindrome(inputString):
    
    if len(inputString) == 1:
        return True
    
    if inputString == inputString[::-1]:
    	return True

    return False

string = raw_input().strip()

print checkPalindrome(string)