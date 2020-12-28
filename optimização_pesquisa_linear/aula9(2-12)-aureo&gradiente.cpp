#include <iostream>
#include <cmath>
#include <vector> 
#include <math.h>

using namespace std;

double f1(double x) {
    return (2*pow(x,2)+1)-5*cos(10*x);
}

//Condição de paragem deveria ser enquanto que o valor de xn for diferente que o valor máximo de x no integral

double aurea_minimo(double x1, double x2)
{
    cout << "AREUA min:";

    double b = (sqrt(5) - 1)/2;
    double a = pow(b,2);

    double x3, x4;

    while (abs(x1-x2)>0.0001) {
        x3 = x1 + a*(x2 - x1);
        x4 = x1 + b*(x2 - x1);
        if (f1(x3) < f1(x4)) x2 = x4;
        else x1 = x3;

    }
    cout << "min: " << x1 << "\n";
    return x1;

}

double aurea_maximo(double x1, double x2)
{
    cout << "AREUA max:";

    double b = (sqrt(5) - 1) / 2;
    double a = pow(b, 2);

    double x3, x4;

    while (abs(x1 - x2) > 0.0001) {
        x3 = x1 + a * (x2 - x1);
        x4 = x1 + b * (x2 - x1);
        if (f1(x3) < f1(x4)) x1 = x3;
        else x2 = x4;

    }
    cout << "max: " << x1 << "\n";
    return x1;

}

double f2(double x, double y) {
    return pow(y,2)-2*x*y-6*y+2*pow(x,2)+12;
}

double f2_x(double x, double y) {
    return -2 * y + 4 * x;
}

double f2_y(double x, double y) {
    return 2 * y - 2 * x - 6;
}

double op_multi(double x1, double y1) {
    double x2=x1, y2=y1, h=1;

    do {
        x1 = x2;
        y1 = y2;
        x2 = x1 - h*f2_x(x1,y1);
        y2 = y1 - h*f2_y(x1, y1);
        if (f2(x2, y2) < f2(x1, y1)) {
            h = h * 2;
        }
        else {
            h = h / 2;
        }
    } while ((abs(x2 - x1) >= 0.01) || (abs(y2 - y1) >= 0.01));

    cout << "x2: " << x2;
    cout << "y2: " << y2;

    return x2;
}


int main() {
    aurea_minimo(-1.0, 0.0);
    aurea_maximo(-1.0, 0.0);

    op_multi(0, 0);
    return 0;
}