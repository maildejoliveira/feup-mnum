#include <iostream>
#include <cmath>
#include <vector> 
#include <math.h>

using namespace std;

# define M_PI   3.14159265358979323846  /* pi */

double f(double x) {
    return sin(x) / pow(x,2);
}

double trap_method(int n,  double xo, double xn) 
{
    cout << "Method Trapezios:" << endl;
    int n_=1;
    double h = (xn - xo) / n;
    double s_t = f(xo);
    while (n_<=n-1) {
        s_t += 2*f(xo + n_ * h);
        n_++;
    }
    s_t += f(xn);
    s_t = s_t*(h/2);

    cout << "n: " << n << endl;
    cout << "Trap: " << s_t << endl << endl;

    return s_t;
}

double simp_method(int n, double xo, double xn)
{
    cout << "Method Simpson:" << endl;
    int n_ = 1;
    double h = (xn - xo) / n;
    double s_s = f(xo);
    while (n_ <= n-1) {
        if((n_%2)==0)
            s_s += 2*f(xo + (n_ * h));
        else 
            s_s += 4*f(xo + (n_ * h));
        n_++;
    }
    s_s += f(xn);
    s_s = s_s*(h/3);

    cout << "n: " << n << endl;
    cout << "SIMP: " << s_s << endl << endl;

    return s_s;
}

double quociente(double s, double s_, double s__) 
{
    return ((s_ - s) / (s__ - s_));
}

double erro(int ordem, double s__, double s_) 
{
    return ((s__ - s_) / (pow(2, ordem) - 1));
}


int main() {
    double st, st_, st__;
    cout << "TRAPEZIOS" << endl << endl;
    st = trap_method(4, M_PI/2 , M_PI );
    st_ = trap_method(8, M_PI / 2, M_PI);
    st__ = trap_method(16, M_PI / 2, M_PI);
    cout << "QC TRAPEZIOS: " << quociente(st, st_, st__) << endl << endl;
    cout << "ERRO: " << erro(2, st__, st_) << endl << endl;

    double ss, ss_, ss__;
    cout << "SIMPSON" << endl << endl;
    ss = simp_method(4, M_PI/2, M_PI );
    ss_ = simp_method(8, M_PI / 2, M_PI);
    ss__ = simp_method(16, M_PI / 2, M_PI);
    cout << "QC SIMPSON: " << quociente(ss, ss_, ss__) << endl << endl;
    cout << "ERRO: " << erro(4, ss__, ss_) << endl << endl;

}