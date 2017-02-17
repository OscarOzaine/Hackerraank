import sys

class Stack:
    
    brackets = []
        
    def push(self, item):
        self.brackets.append(item)
        
    def pop(self):
        return self.brackets.pop()
    
    def get_last(self):
        return self.brackets[-1]
        
    def length(self):
        return len(self.brackets)

    def is_empty(self):
        return (self.brackets == [])
    
    def _print(self):
        print self.brackets
    

def is_matched(expression):
    
    if len(expression) % 2 != 0:
        return False
    
    is_open_bracket = ['[', '{', '(']
    is_close_bracket = [']', '}', ')']
    balanced = 0
    
    result = Stack()
    
    for exp in expression:
        if balanced == 0 and exp not in is_open_bracket:
            return False

        if exp in is_open_bracket:
            result.push(exp)
            balanced += 1
        elif exp in is_close_bracket:
            
            if result.length() < 1:
                result.push(exp)
            elif is_open_bracket.index(result.get_last()) == is_close_bracket.index(exp):
                result.pop()
                balanced -= 1
            
    if balanced:
        return False
    else:
        return True

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
