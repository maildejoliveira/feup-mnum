#include <iostream>
#include <cmath>
#include <vector> 

using namespace std;

#define STOP 0.0001

void gaussJacobi(double x1, double x2, double x3)
{
    cout << "GAUSS-JACOBI:" << endl;
    //vector<double> eq1 = { 3.0,1.0,1.0,7.0 }, eq2 = { 1.0,4.0,2.0,4.0 }, eq3 = { 0.0,2.0,5.0, 5.0 };
    vector<double> eq1 = { 7.0,2.0,0.0,24.0 }, eq2 = { 4.0,10.0,1.0,27.0 }, eq3 = { 5.0,-2.0,8.0,27.0 }; //exemplo livro
    double x1_ = x1, x2_ = x2, x3_ = x3;
    int n = 0;
    do {
        n++;
        x1 = x1_;
        x2 = x2_;
        x3 = x3_;
        x1_ = (eq1[3] - eq1[1] * x2 - eq1[2] * x3) / eq1[0];
        x2_ = (eq2[3] - eq2[0] * x1 - eq2[2] * x3) / eq2[1];
        x3_ = (eq3[3] - eq3[0] * x1 - eq3[1] * x2) / eq3[2];
    } while ((abs(x1_ - x1) > 0.0001) | (abs(x2 - x2_) > 0.0001) | (abs(x3 - x3_) > 0.0001));

    cout << "n: " << n << endl;
    cout << "x1: " << x1_ << endl;
    cout << "x2: " << x2_ << endl;
    cout << "x3: " << x3_ << endl;
}

void gaussSeidel(float x1, float x2, float x3)
{
    cout << "GAUSS-JACOBI:" << endl;
    //vector<double> eq1 = { 3.0,1.0,1.0,7.0 }, eq2 = { 1.0,4.0,2.0,4.0 }, eq3 = { 0.0,2.0,5.0, 5.0 };
    vector<double> eq1 = { 7.0,2.0,0.0,24.0 }, eq2 = { 4.0,10.0,1.0,27.0 }, eq3 = { 5.0,-2.0,8.0,27.0 }; //exemplo livro
    double x1_ = x1, x2_ = x2, x3_ = x3;
    int n = 0;
    do {
        n++;
        x1 = x1_;
        x2 = x2_;
        x3 = x3_;
        x1_ = (eq1[3] - eq1[1] * x2 - eq1[2] * x3) / eq1[0];
        x2_ = (eq2[3] - eq2[0] * x1_ - eq2[2] * x3) / eq2[1];
        x3_ = (eq3[3] - eq3[0] * x1_ - eq3[1] * x2_) / eq3[2];
    } while ((abs(x1_ - x1) > 0.0001) | (abs(x2 - x2_) > 0.0001) | (abs(x3 - x3_) > 0.0001));

    cout << "n: " << n << endl;
    cout << "x1: " << x1_ << endl;
    cout << "x2: " << x2_ << endl;
    cout << "x3: " << x3_ << endl;
}

int main() {
    gaussJacobi(0, 0, 0);
    cout << "############################" << endl;
    gaussSeidel(0, 0, 0);
    return 0;
}