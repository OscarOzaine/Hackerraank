## Day 19: Interfaces
## https://www.hackerrank.com/challenges/30-interfaces

class Calculator:public AdvancedArithmetic
{
    public:
        int divisorSum(int n);
};

int Calculator::divisorSum(int n)
{
    int sum = 0;
    int x = n;
    while(x > 0) {
        if (n % x == 0) {
            sum = sum + x;
        }
        x--;
    }
    
    return sum;
}

