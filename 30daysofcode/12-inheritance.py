
class Student(Person):
    firstName = ''
    lastName = ''
    idNum = ''
    scores = ''
    
    def __init__(self, firstName, lastName, idNum, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNum = idNum
        self.scores = scores
        
    def printPerson(self):
        print 'Name: ' + self.lastName + ', ' + self.firstName
        print 'ID: ' + self.idNum
        
    def calculate(self):
        grade = sum(self.scores) / len(self.scores)
        
        if grade >= 90 and grade <= 100:
            grade = 'O'
        elif grade >= 80 and grade <= 89:
            grade = 'E'
        elif grade >= 70 and grade <= 79:
            grade = 'A'
        elif grade >= 55 and grade <= 69:
            grade = 'P'
        elif grade >= 40 and grade <= 54:
            grade = 'D'
        elif grade < 40:
            grade = 'T'
            
        return grade
