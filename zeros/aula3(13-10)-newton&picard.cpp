#include <iostream>
#include <cmath>

using namespace std;

double f(double a)
{
	return a-2*log(a)-5;
	//return pow(2, sqrt(a)) - 10 * a + 1;
	//return (1 / tan(a)) * sin(3*a) - a + 1;
}

double f_(double a) //derivadas
{
	return 1 - 2 / a;
}

double g(double a) { //metodo de picard peano funçao 1 , x=9
	return 2 * log(a) + 5;
}


int newton() // newton method
{
	double l_x = 9, x = 9;
	int counter = 0;

	do
	{
		x = l_x;
		counter++;
		l_x = x - f(x) / f_(x);
		cout << x << endl;
	} while (std::abs(l_x - x) > 0.000001);
	
	return 0;
}

int picard() { // Picard_peano

	double l_x = 9, x = 9;
	int counter = 0;

	do
	{
		x = l_x;
		counter++;
		l_x = g(x);
		cout << x << endl;
	} while (std::abs(l_x - x) > 0.000001);

	return 0;
}

int main()
{

}