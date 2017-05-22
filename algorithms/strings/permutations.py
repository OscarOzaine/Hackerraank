'''
void permutate( char[] str, int index )
{
    int i = 0;
    if( index == strlen(str) )
    { // We have a permutation so print it
        printf(str);
        return;
    }
    for( i = index; i < strlen(str); i++ )
    {
        swap( str[index], str[i] );
        permutate( str, index + 1 );
        swap( str[index], str[i] );
    }
} 

permutate( "abcdefgh", 0 );
'''

def swap(string, i, j):
    lst = list(string);
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)

def permutate(string, index):
    string = list(string)

    i = 0
    if index == len(string):
        print ''.join(string)
        return ''.join(string)

    x = index

    for x in range(index, len(string)):
        #print x, string, string[x]
        #print index, string, string[index]

        #temp = string[x]
        swap(string, index, x)
        permutate(''.join(string), index + 1)
        swap(string, index, x)
        

print permutate('abcde', 0)