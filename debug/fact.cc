#include<iostream>
 
using namespace std;
 
long factorial(int n);
 
int main()
{
    int n(3);
//    cin>>n;
    long val=factorial(n);
    std::cout<<val;
    cin.get();
    return 0;
}
 
long factorial(int n)
{
    long result(1);
    while(n--)
    {
        result*=n;
    }
    return result;
}
