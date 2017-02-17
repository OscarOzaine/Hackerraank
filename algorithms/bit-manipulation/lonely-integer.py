
def lonelyinteger(a):
    sol = 0
    for n in a:
        sol ^= n;
        
    return sol;

if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
