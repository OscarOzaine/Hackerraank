
n = int(raw_input().strip())

dictionary = dict()

for i in range(0, n):
    the_input = raw_input().strip().split(' ')
    dictionary[the_input[0]] = the_input[1]
    
for i in range(0, n):
    name = raw_input().strip()
    if name in dictionary:
        print str(name) + '=' + dictionary[name]
    else:
        print 'Not found'
    
    