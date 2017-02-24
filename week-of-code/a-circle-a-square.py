#!/bin/python

import sys
from math import sqrt

w,h = raw_input().strip().split(' ')
w,h = [int(w), int(h)]
circleX, circleY, r = raw_input().strip().split(' ')
circleX, circleY, r = [int(circleX), int(circleY), int(r)]
x1, y1, x3, y3 = raw_input().strip().split(' ')
x1, y1, x3, y3 = [int(x1), int(y1), int(x3), int(y3)]

def isInCircle(i, j):
    #x = ()
    
    j = ((j + 0.5) + (j - 0.5))/2
    i = ((i + 0.5) + (i - 0.5))/2
    dist = ((j - circleX)**2 + (i - circleY)**2)
    dist = sqrt(dist)
    #x = ((circleX - 0.5) - (j - 0.5))**2
    #y = ((circleY - 0.5) - (i - 0.5))**2
    
    #dist = sqrt(x + y)
    
    if float(dist) <= float(r):
        return True
    
    return False


def isInside(x1, y1, x2, y2, x3, y3, x, y):
    
    denominator = ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))
    a = ((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / denominator
    b = ((y3 - y1) * (x - x3) + (x1 - x3) * (y - y3)) / denominator
    c = 1 - a - b
        
    return 0 <= a and a <= 1 and 0 <= b and b <= 1 and 0 <= c and c <= 1;
    
def isInSquare(i, j):
    i = float(i) 
    j = float(j)
              
              
    cx = (x1+x3) / 2
    cy = (y1+y3) / 2
    
    vx = x1 - cx
    vy = y1 - cy
    ##given 2 points - get other 2 points
    ux = vy
    uy = -vx #rotate through 90 degrees
    
    x2 = cx + ux #one of the endpoints of other diagonal
    y2 = cy + uy
    
    x4 = cx - ux #the other endpoint
    y4 = cy - uy
    
    if isInside(x1, y1, x2, y2, x3, y3, j, i):
        return True
    elif isInside(x1, y1, x4, y4, x3, y3, j, i):
        return True
    
    return False


for i in range(0, h):
    for j in range(0, w):
        if isInCircle(i, j):
            sys.stdout.write('#')
        elif isInSquare(i, j):
            sys.stdout.write('#')
        else:
            sys.stdout.write('.')
    print 

