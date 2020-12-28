#include <iostream>
#include <cmath>
#include <vector> 
#include <math.h>

using namespace std;

double f(double x,double y) {
    return (pow(y,2)-2*x*y-6*y+2*pow(x,2)+12+cos(4*x));
}
double f2(double x, double y) {
    return pow((x + 1),2) + pow((y - 4), 2);
}

double gradx(double x, double y) {
    return (-2 * y - 4 * sin(4 * x) + 4 * x);
}

double gradx2(double x, double y) {
    return 2 * (x + 1);
}

double grady(double x, double y) {
    return (2 * y -2 * x- 6);
}

double grady2(double x, double y) {
    return 2 * (y - 4);
}

double hxx_in(double x, double y) {
    return 2 / (2 * (4 - 16 * cos(4 * x)) - 4);
}

double hxx_in2(double x, double y) {
    return 0.5;
}

double hxy_in(double x, double y) {
    return 2 / (2 * (4 - 16 * cos(4 * x)) - 4);
}

double hxy_in2(double x, double y) {
    return 0;
}

double hyx_in(double x, double y) {
    return 2 / (2 * (4 - 16 * cos(4 * x)) - 4);
}

double hyx_in2(double x, double y) {
    return 0;
}

double hyy_in(double x, double y) {
    return (4 - 16 * cos(4 * x))/ (2 * (4 - 16 * cos(4 * x)) - 4);
}

double hyy_in2(double x, double y) {
    return 0.5;
}

double met_quadrica(double x0, double y0) {

    cout << "MET QUADRATICO" << endl;
    
    double x1 = x0, y1 = y0;
    int counter = 0;

    do {
        counter++;
        x0 = x1;
        y0 = y1;
        x1 = x0 - (hxx_in(x0, y0) * gradx(x0, y0) + hxy_in(x0, y0) * grady(x0, y0));
        y1 = y0 - (hyx_in(x0, y0) * gradx(x0, y0) + hyy_in(x0, y0) * grady(x0, y0));
    } while ((abs(x1 - x0) >= 0.0001) || (abs(y1 - y0) >= 0.0001));

    cout << "x1: " << x1 << endl;
    cout << "y1: " << y1 << endl;
    cout << "c: " << counter << endl;

    return x1;
}

double met_lm(double x0, double y0) {

    cout << "LM" << endl;

    double x1 = x0, y1 = y0, h=0.05;
    int counter = 0;

    do {
        counter++;
        x0 = x1;
        y0 = y1;
        x1 = x0 - (hxx_in(x0, y0) * gradx(x0, y0) + hxy_in(x0, y0) * grady(x0, y0) + h * (gradx(x0, y0)));
        y1 = y0 - (hyx_in(x0, y0) * gradx(x0, y0) + hyy_in(x0, y0) * grady(x0, y0) + h * (grady(x0, y0)));
        if (f(x1, y1) > f(x0, y0)) {
            h *= 2;
        }
        else {
            h /= 2;
        }
    } while ((abs(x1 - x0) >= 0.0001) || (abs(y1 - y0) >= 0.0001));

    cout << "x1: " << x1 << endl;
    cout << "y1: " << y1 << endl;
    cout << "c: " << counter << endl;

    return x1;
}


int main() {
    met_quadrica(1, 1);
    met_lm(1, 1);
    //met_lm(0, 0); //2
    return 0;
}