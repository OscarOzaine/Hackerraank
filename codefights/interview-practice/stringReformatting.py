def stringReformatting(s, k):
    
    counter = 0
    res = []
    for i in reversed(s):
        if i != '-':
            if counter == k - 1:
                res.append(i)
                res.append('-')
                counter = 0
            else:
                res.append(i)
                counter += 1
    
    if len(res) > 0:
        if res[len(res) - 1] == '-':
            res = res[:len(res) - 1]
    return ''.join(reversed(res))
                

