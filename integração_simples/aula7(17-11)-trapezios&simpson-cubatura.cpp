#include <iostream>
#include <cmath>
#include <vector> 
#include <math.h>

using namespace std;

# define M_PI   3.14159265358979323846  /* pi */

double f(double x, double y) {
    return exp(y-x);
}

double trap_method_multiples(double xo, double xn, double yo, double yn, double nx, double ny) 
{
    cout << "Method Trapezios:" << endl;
    double hx = (xn - xo) / nx;
    double hy = (yn - yo) / ny;

    double e0; //soma dos valores da função nos vértices da malha
    double e1; //soma dos valores da função nos pontos médios da malha
    double e2; //valor da função no centro da malha

    //calculo da soma dos valores da função nos 4 vértices da malha
    e0 = f(xo, yo) + f(xo, yn) + f(xn, yo) + f(xn, yn);

    //calculo da soma dos valores da função nos 4 pontos médios da malha , neste caso
    e1 = f(xo+hx, yo) + f(xo, yo+hy) + f(xn, yo+hy) + f(xo+hx, yn);

    //calculo do valor da função no centro da malha
    e2 = f(xo + hx, yo + hy);

    double s_t = ((hx * hy) / 4) * (e0 + 2 * e1 + 4 * e2);

    cout << "ST: " << s_t << endl << endl;
    return s_t;
}

double simp_method_multiples(double xo, double xn, double yo, double yn, double nx, double ny)
{
    cout << "Method Simpson:" << endl;
    double hx = (xn - xo) / nx;
    double hx_=0;
    double hy = (yn - yo) / ny;
    double hy_=0;

    double e0; //soma dos valores da função nos vértices da malha
    double e1; //soma dos valores da função nos pontos médios da malha
    double e2; //valor da função no centro da malha

    //calculo da soma dos valores da função nos 4 vértices da malha
    e0 = f(xo, yo) + f(xo, yn) + f(xn, yo) + f(xn, yn);

    //calculo da soma dos valores da função nos 4 pontos médios da malha , neste caso
    e1 = f(xo + hx, yo) + f(xo, yo + hy) + f(xn, yo + hy) + f(xo + hx, yn);

    //calculo do valor da função no centro da malha
    e2 = f(xo + hx, yo + hy);

    double s_s = ((hx * hy) / 9) * (e0 + 4 * e1 + 16 * e2);

    cout << "SS: " << s_s << endl << endl;
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

//NOTA: neste métodos tamos a supor apenas uma uma malha de quatro cadernos 
//no entanto se o n for para maior que 2 temos que por recursão analisar as diferentes malhas
//se for impar deduzir as expressões

int main() {
    double st, st_, st__;
    cout << "TRAPEZIOS" << endl << endl;
    st = trap_method_multiples(0,0.5,0,0.5,2,2);
    st_ = trap_method_multiples(0, 0.5, 0, 0.5, 4, 4);
    st__ = trap_method_multiples(0, 0.5, 0, 0.5, 8, 8);
    cout << "QC TRAPEZIOS: " << quociente(st, st_, st__) << endl << endl;
    cout << "ERRO: " << erro(2, st__, st_) << endl << endl;

    double ss, ss_, ss__;
    cout << "SIMPSON" << endl << endl;
    ss = simp_method_multiples(0, 0.5, 0, 0.5, 2, 2);
    ss_ = simp_method_multiples(0, 0.5, 0, 0.5, 4, 4);
    ss__ = simp_method_multiples(0, 0.5, 0, 0.5, 8, 8);
    cout << "QC SIMPSON: " << quociente(ss, ss_, ss__) << endl << endl;
    cout << "ERRO: " << erro(4, ss__, ss_) << endl << endl;

}