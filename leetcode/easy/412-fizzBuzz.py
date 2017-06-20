class Solution(object):
    def fizzBuzz(self, n):
        
        res = []
        
        for i in range(1, n + 1):
            tmp = ''
            if i % 3 == 0:
                tmp += 'Fizz'
            if i % 5 == 0:
                tmp += 'Buzz'
            if tmp == '':
                tmp += str(i)

            res.append(tmp)

        return res

