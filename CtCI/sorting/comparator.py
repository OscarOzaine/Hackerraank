
class Checker:
    a = None
    b = None
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def comparator(self):
        
        if self.a.score == self.b.score:
            if self.a.name > self.b.name:
                return 1
            elif self.b.name > self.a.name:
                return -1
        
        elif self.a.score > self.b.score:
            return -1
        elif self.b.score > self.a.score:
            return 1
        
        return 0
        

class Player:
    name = None
    score = None
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def comparator(a, b):
        checker = Checker(a, b)
        
        return checker.comparator()
        
        