# include <iostream>
using namespace std;

int main(){
    int var = 20;
    int *ip;

    ip = &var;

    cout << "Value of Var var: ";
    cout << var << endl;

    cout << "Value of stored in ip var: ";
    cout << ip << endl;
 
    
    cout << "Value of *ip variable: ";
    cout << *ip << endl;

    return 0;
} 
