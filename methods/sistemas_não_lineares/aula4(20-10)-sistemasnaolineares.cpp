#include <iostream>
#include <cmath>

using namespace std;

double f1(double x, double y) {
	return 2 * pow(x, 2) - x * y - 5 * x + 1;
}

double f2(double x, double y) {
	return x + 3 * log(x) - pow(y,2);
}

double f1_x(double x, double y) {
	return -y + 4 * x - 5;
}

double f1_y(double x, double y) {
	return -x;
}

double f2_x(double x, double y) {
	return 3 / x + 1;
}

double f2_y(double x, double y) {
	return -2 * y;
}


double g1(double x, double y) { //x=g1(x,y)
	return sqrt((x * y + 5 * x - 1 )/ 2);
}

double g2(double x, double y) {  //y=g2(x,y)
	return sqrt(x + 3 * log(x));
}

int newton_sistemas_naolineares() // newton method
{
	double l_x = 4, x = 4;
	double l_y = 4, y = 4;
	int counter = 1;

	do
	{
		x = l_x;
		y = l_y;
		counter++;
		l_x = x - (f1(x, y) * f2_y(x, y) - f2(x, y) * f1_y(x, y)) / (f1_x(x, y) * f2_y(x, y) - f2_x(x, y) * f1_y(x, y));
		l_y = y - (f2(x, y) * f1_x(x, y) - f1(x, y) * f2_x(x, y)) / (f1_x(x, y) * f2_y(x, y) - f2_x(x, y) * f1_y(x, y));
		cout << "x: " << x << endl;
		cout << "y: " << y << endl;
		cout << counter << endl;

	} while ((std::abs(l_x - x) > 0.000001) && (std::abs(l_y - y) > 0.000001));

	return 0;
}

int picard_sistemas_naolineares() // newton method
{
	double l_x = 4, x = 4;
	double l_y = 4, y = 4;
	int counter = 0;
	do
	{
		x = l_x;
		y = l_y;
		counter++;
		l_x = g1(x,y);
		l_y = g2(x,y);
		cout << "x: " << x << endl;
		cout << "y: " << y << endl;
		cout << counter << endl;
	} while ((std::abs(l_x - x) > 0.000001) && (std::abs(l_y - y) > 0.000001));
	return 0;
}

int gauss_sidel_sistemas_naolineares() // newton method
{
	double l_x = 4, x = 4;
	double l_y = 4, y = 4;
	int counter = 0;
	do
	{
		x = l_x;
		y = l_y;
		counter++;
		l_x = g1(x, y);
		l_y = g2(l_x, y);
		cout << "x: " << x << endl;
		cout << "y: " << y << endl;
		cout << counter << endl;
	} while ((std::abs(l_x - x) > 0.000001) && (std::abs(l_y - y) > 0.000001));
	return 0;
}


int main() {
	//newton_sistemas_naolineares();
	picard_sistemas_naolineares();
	//gauss_sidel_sistemas_naolineares();
}