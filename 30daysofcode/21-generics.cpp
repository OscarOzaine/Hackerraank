/**
*    Name: printArray
*    Print each element of the generic vector on a new line. Do not return anything.
*    @param A generic vector
**/

template<class T> void printArray(std::vector<T> vect)
{
    int i;
    for(i=0; i < vect.size(); i++) {
        cout << vect[i] << endl;
    }
}

