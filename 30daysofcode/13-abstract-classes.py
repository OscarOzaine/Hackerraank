##Day 13: Abstract Classes
##https://www.hackerrank.com/challenges/30-abstract-classes

class MyBook:
    
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        
    def display(self):
        print 'Title: ' + str(self.title)
        print 'Author: ' + str(self.author)
        print 'Price: ' + str(self.price)