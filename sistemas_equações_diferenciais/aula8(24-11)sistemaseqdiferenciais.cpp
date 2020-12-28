#include <iostream>
#include <cmath>
#include <vector> 
#include <math.h>

using namespace std;

double f(double x, double y, double z) {
    return z;
}

double g(double x, double y, double z) {
    return x-3*z-2*y;
}

//Condição de paragem deveria ser enquanto que o valor de xn for diferente que o valor máximo de x no integral

double euleryn(double xo, double yo, double zo, double h, double b) //a e b limites de integração
{
    cout << "EULER:";

    double xn = xo, y_, z_, yn=yo , zn=zo ;

    while (abs(b-xn)>0.000001) {
        y_ = f(xn, yn, zn);
        z_ = g(xn, yn, zn);
        xn += h;
        yn = yn + h * y_;
        zn = zn + h * z_;
    }
    cout << "yn: " << yn << endl;
    return yn;

}
double eulerzn(double xo, double yo, double zo, double h, double b) //a e b limites de integração
{
    cout << "EULER:";

    double xn = xo, y_, z_, yn = yo, zn = zo;

    while (abs(b - xn) > 0.000001) {
        y_ = f(xn, yn, zn);
        z_ = g(xn, yn, zn);
        xn += h;
        yn = yn + h * y_;
        zn = zn + h * z_;
    }
    cout << "zn: " << zn << endl;

    return zn;

}

double rk2yn(double xo, double yo, double zo, double h, double b) //a e b limites de integração
{
    cout << "RK2:";

    double xn = xo, y_, z_, yn = yo, zn = zo, xaux, yaux;

    while (abs(b - xn) > 0.000001) {
        xaux = xn;
        yaux = yn;
        y_ = f(xn, yn, zn);
        z_ = g(xn, yn, zn);
        xn += h;
        yn = yn + h * f(xaux + h/2, yaux + (h/2)*y_, zn + (h/2)*z_);
        zn = zn + h * g(xaux + h / 2, yaux + (h / 2) * y_, zn + (h / 2) * z_);
    }
    cout << "yn: " << yn << endl;
    return yn;
}
double rk2zn(double xo, double yo, double zo, double h, double b) //a e b limites de integração
{
    cout << "RK2:";

    double xn = xo, y_, z_, yn = yo, zn = zo;

    while (abs(b - xn) > 0.000001) {
        y_ = f(xn, yn, zn);
        z_ = g(xn, yn, zn);
        yn = yn + h * f(xn + h / 2, yn + (h / 2) * y_, zn + (h / 2) * z_);
        zn = zn + h * g(xn + h / 2, yn + (h / 2) * y_, zn + (h / 2) * z_);
        xn += h;
    }
    cout << "zn: " << zn << endl;
    return zn;
}


double rk4yn(double xo, double yo, double zo, double h, double b){
    cout << "RK4 YN:";

    double xn = xo, yn = yo, zn = zo, y_, z_, y1, y2, y3, y4, z1, z2, z3, z4;
    double xaux = xo, yaux = yo, zaux = zo;

    while (abs(b - xn) > 0.000001) {
        xaux = xn;
        yaux = yn;
        zaux = zn;
        xn = xn + h;
        y1 = h * f(xaux, yaux, zaux);
        z1 = h * g(xaux, yaux, zaux);
        y2 = h * f(xaux + (h / 2), yaux + (y1 / 2), zaux + (z1/2));
        z2 = h * g(xaux + (h / 2), yaux + (y1 / 2), zaux + (z1/2));
        y3 = h * f(xaux + (h / 2), yaux + (y2 / 2), zaux + (z2/2));
        z3 = h * g(xaux + (h / 2), yaux + (y2 / 2), zaux + (z2/2));
        y4 = h * f(xaux + h, yaux + y3, zaux + z3);
        z4 = h * g(xaux + h, yaux + y3, zaux + z3);
        
        y_ = y1 / 6 + y2 / 3 + y3 / 3 + y4 / 6;
        z_ = z1 / 6 + z2 / 3 + z3 / 3 + z4 / 6;
        yn = yn + y_;
        zn = zn + z_;
    }

    cout << "yn: " << yn << endl;
    return yn;
}
double rk4zn(double xo, double yo, double zo, double h, double b) {
    cout << "RK4 ZN:";

    double xn = xo, yn = yo, zn = zo, y_, z_, y1, y2, y3, y4, z1, z2, z3, z4;
    double xaux = xo, yaux = yo, zaux = zo;

    while (abs(b - xn) > 0.000001) {
        xaux = xn;
        yaux = yn;
        zaux = zn;
        xn = xn + h;
        y1 = h * f(xaux, yaux, zaux);
        z1 = h * g(xaux, yaux, zaux);
        y2 = h * f(xaux + (h / 2), yaux + (y1 / 2), zaux + (z1 / 2));
        z2 = h * g(xaux + (h / 2), yaux + (y1 / 2), zaux + (z1 / 2));
        y3 = h * f(xaux + (h / 2), yaux + (y2 / 2), zaux + (z2 / 2));
        z3 = h * g(xaux + (h / 2), yaux + (y2 / 2), zaux + (z2 / 2));
        y4 = h * f(xaux + h, yaux + y3, zaux + z3);
        z4 = h * g(xaux + h, yaux + y3, zaux + z3);

        y_ = y1 / 6 + y2 / 3 + y3 / 3 + y4 / 6;
        z_ = z1 / 6 + z2 / 3 + z3 / 3 + z4 / 6;
        yn = yn + y_;
        zn = zn + z_;
    }

    cout << "zn:" << zn << endl;
    return zn;
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
    double sy, sy_, sy__, sz, sz_, sz__;
    sy = euleryn(0, 0, 0, 0.025, 0.5);
    sy_ = euleryn(0, 0, 0, 0.0125, 0.5);
    sy__ = euleryn(0, 0, 0, 0.00625, 0.5);

    cout << "QC EULER YN: " << quociente(sy, sy_, sy__) << endl;
    cout << "ERRO: " << erro(1, sy__, sy_) << endl << endl;

    double s, s_, s__, yn, zn;
    sz = eulerzn(0, 0, 0, 0.025, 0.5);
    sz_ = eulerzn(0, 0, 0, 0.0125, 0.5);
    sz__ = eulerzn(0, 0, 0, 0.00625, 0.5);
  
    cout << "QC EULER ZN: " << quociente(sz, sz_, sz__) << endl;
    cout << "ERRO: " << erro(1, sz__, sz_) << endl << endl;

    sy = rk2yn(0, 0, 0, 0.025, 0.5);
    sy_ = rk2yn(0, 0, 0, 0.0125, 0.5);
    sy__ = rk2yn(0, 0, 0, 0.00625, 0.5);


    cout << "QC RK2 YN: " << quociente(sy, sy_, sy__) << endl;
    cout << "ERRO: " << erro(2, sy__, sy_) << endl << endl;

    sz = rk2zn(0, 0, 0, 0.025, 0.5);
    sz_ = rk2zn(0, 0, 0, 0.0125, 0.5);
    sz__ = rk2zn(0, 0, 0, 0.00625, 0.5);

    cout << "QC RK2 ZN: " << quociente(sz, sz_, sz__) << endl;
    cout << "ERRO: " << erro(2, sz__, sz_) << endl << endl;

    sy = rk4yn(0, 0, 0, 0.025, 0.5);
    sy_ = rk4yn(0, 0, 0, 0.0125, 0.5);
    sy__ = rk4yn(0, 0, 0, 0.00625, 0.5);

    cout << "QC RK4 YN: " << quociente(sy, sy_, sy__) << endl;
    cout << "ERRO: " << erro(4, sy__, sy_) << endl << endl;

    sz = rk4zn(0, 0, 0, 0.025, 0.5);
    sz_ = rk4zn(0, 0, 0, 0.0125, 0.5);
    sz__ = rk4zn(0, 0, 0, 0.00625, 0.5);

    cout << "QC RK4 ZN: " << quociente(sz, sz_, sz__) << endl;
    cout << "ERRO: " << erro(4, sz__, sz_) << endl << endl;

    
    return 0;
}