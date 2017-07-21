
def hasPathWithGivenSum(t, s, thesum = 0):
    
    if t is None:
        return (s == 0)

    ans = 0

    thesum += t.value 

    if thesum == s and t.left == None and t.right == None:
        return True

    if t.left is not None:
        ans = ans or hasPathWithGivenSum(t.left, s, thesum)
    if t.right is not None:
        ans = ans or hasPathWithGivenSum(t.right, s, thesum)

    return ans 