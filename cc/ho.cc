
#include <iostream> 

using namespace std; 


double dv(double x) {
   return -0.5*x;
}



int main() {
    double x = 1.0, p = 0.0 , dt = 0.1, mass = 1.0; 
    int ntime = 10;
    string hello; 
    hello = "hello world";
    std::cout << hello << std::endl ;
    
    for(int i=1; i < ntime; i++) {
        x = x+p/mass*dt;
        p = p-dv(x)*dt;
        cout << x <<'\t' << p << endl;
}
    return 0;
    
}
