#Left Rotation
#Hackerrank.com
#https://www.hackerrank.com/challenges/array-left-rotation

line = raw_input().strip().split(' ')
number = line[0]
rotations = line[1]

array = raw_input().strip().split(' ')

new_array = []
for rotation in range(0, int(rotations)):
    new_array = []
    a = array.pop(0)
    new_array = array
    new_array.append(a)
    array = new_array

print ' '.join(array)
    
