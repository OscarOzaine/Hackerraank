def reverseVowelsOfString(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    mid = (len(s) / 2) - 1
    start = 0
    end = len(s) - 1
    s = list(s)
    while start <= end:
        
        if s[start] in vowels and s[end] in vowels:
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1
        else:
            if s[start] not in vowels:
                start+=1
            elif s[end] not in vowels:
                end-=1
    
    return ''.join(s)
    
