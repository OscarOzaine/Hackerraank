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

def perm(string, i):
    if i == len(string) - 1:
        print ''.join(string)
    else:
        for j in range(i, len(string)):
            string[i], string[j] = string[j], string[i]
            perm(string, i + 1)
            string[i], string[j] = string[j], string[i]

    return string
  
print perm(list('abcde'), 0)
