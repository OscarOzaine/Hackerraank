combinations = []

def combine(terms, accum):
    last = (len(terms) == 1)
    n = len(terms[0])
    for i in range(n):
        item = accum + terms[0][i]
        if last:
            combinations.append(item)
        else:
            combine(terms[1:], item)
            
def pressingButtons(buttons):
    numbers = {}
    numbers[2] = ['a','b','c']
    numbers[3] = ['d','e','f']
    numbers[4] = ['g','h','i']
    numbers[5] = ['j','k','l']
    numbers[6] = ['m','n','o']
    numbers[7] = ['p','q','r','s']
    numbers[8] = ['t','u','v']
    numbers[9] = ['w','x','y','z']
    
    buttons = map(int, list(buttons))
    res = []
    if len(buttons) > 0:
        
        for i in buttons:
            res.append(numbers[i])
    
    if len(res) > 0:
        combine(res, '')
    return combinations