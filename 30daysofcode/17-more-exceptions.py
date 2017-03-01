## Day 17: More Exception
## https://www.hackerrank.com/challenges/30-more-exceptions

class Calculator():
    
    is_active = 0
    def __init__(self):
        self.is_active = 1
    
    def power(self, n, p):
        try:
            if n < 0 or p < 0:
                raise ValueError
            return n ** p
        except ValueError:
            return 'n and p should be non-negative'
        
