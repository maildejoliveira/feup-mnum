#include <iostream>
#include <cmath>
#include <vector> 
#include <math.h>

using namespace std;

double f(double x, double y) {
    return x*x + y*y;
}

//Condição de paragem deveria ser enquanto que o valor de xn for diferente que o valor máximo de x no integral

double euler(double xo, double yo, double h, double b) //a e b limites de integração
{
    cout << "EULER:";

    double xn = xo, yn = yo, y_;

    while (abs(b-xn)>0.000001) {
        y_ = f(xn, yn);
        xn += h;
        yn = yn + h * y_;
    }
    cout << yn << endl;
    return yn;
}

double rk2(double xo, double yo, double h, double b) //a e b limites de integração
{
    cout << "RK2:";

    double xn = xo, yn = yo, y_;
    double tempx = xo, tempy = yo;

    while (abs(b - xn) > 0.000001) {
        tempx = xn;
        tempy = yn;
        xn = tempx + h;
        y_ = f(tempx + (h / 2), tempy + (h / 2) * f(tempx, tempy));
        yn = yn + h * y_;
    }
    cout << yn << endl;
    return yn;
}

double rk4(double xo, double yo, double h, double b) //a e b limites de integração
{
    cout << "RK4:";

    double xn = xo, yn = yo, y_, y1, y2, y3, y4;
    double tempx = xo, tempy = yo;

    while (abs(b - xn) > 0.000001) {
        tempx = xn;
        tempy = yn;
        xn = tempx + h;
        y1 = h * f(tempx, tempy);
        y2 = h * f(tempx + (h / 2), tempy + (y1 / 2));
        y3 = h * f(tempx + (h / 2), tempy + (y2 / 2));
        y4 = h * f(tempx + h, tempy + y3);
        y_ = y1 / 6 + y2 / 3 + y3 / 3 + y4 / 6;
        yn = yn + y_;
    }
    cout << yn << endl;
    return yn;
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
    double s, s_, s__;
    s = euler(0, 0, 0.1, 1.4);
    s_ = euler(0, 0, 0.05,1.4);
    s__ = euler(0, 0, 0.025,1.4);
  
    cout << "QC EULER: " << quociente(s, s_, s__) << endl << endl;
    cout << "ERRO: " << erro(1, s__, s_) << endl << endl;

    s = rk2(0, 0, 0.1, 1.4);
    s_ = rk2(0, 0, 0.05, 1.4);
    s__ = rk2(0, 0, 0.025, 1.4);

    cout << "QC RK2: " << quociente(s, s_, s__) << endl << endl;
    cout << "ERRO: " << erro(2, s__, s_) << endl << endl;

    s = rk4(0, 0, 0.1, 1.4);
    s_ = rk4(0, 0, 0.05, 1.4);
    s__ = rk4(0, 0, 0.025, 1.4);

    cout << "QC RK2: " << quociente(s, s_, s__) << endl << endl;
    cout << "ERRO: " << erro(4, s__, s_) << endl << endl;

    return 0;
}