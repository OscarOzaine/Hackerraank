def isCryptSolution(crypt, solution):
    dictionary = {}
    for s in solution:
        dictionary[s[0]] = s[1]
    
    nums = []
    for c in crypt:
        str = ''
        for i in c:
            str += dictionary[i]
        nums.append(str)
        
    for n in nums:
        if n[0] == '0' and len(n)>1:
            return False
    
    num = int(nums[0]) + int(nums[1])
    
    if int(num) != int(nums[2]):
        return False
    
    if nums[2][0] == '0' and len(nums[2])>1:
        return False
    
    return True

