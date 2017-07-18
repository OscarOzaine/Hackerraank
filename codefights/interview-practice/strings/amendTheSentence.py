def amendTheSentence(s):
    string = ''
    s = list(s)
    for i in s:
        if i.isupper():
            string += ' ' + i.lower()
        else:
            string += i
            
    return string.strip()

