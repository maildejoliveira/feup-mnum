#include <math.h>
#include <iostream>

double f(double x) {
	return x - 2 * log(x) - 5; //1
	//return pow(2, sqrt(x)) - 10 * x + 1; //2
	//return 1.0 / tan(x) * sin(3 * x) - x + 1; //3
}

int bissec_absolutstop(double a, double b) {
	int n=0;
	double m;
	while (std::abs(b-a) > 0.000001)
	{
		m = (a + b) / 2;
		if (f(a)*f(m)<0)
		{
			b=m;
		}
		else
		{
			a =m;
		}
		n++;
	}
	std::cout << "a: " << a << std::endl;
	std::cout << "b: " << b << std::endl;
	std::cout << "counter: " << n << std::endl << std::endl;
	return 0;
}

int bissec_nullfunction(double a, double b) {
	int n = 0;
	double m;
	while (std::abs(f(b) - f(a)) > 0.000001)
	{
		m = (a + b) / 2;
		if (f(a) * f(m) < 0)
		{
			b = m;
		}
		else
		{
			a = m;
		}
		n++;
	}
	std::cout << "a: " << a << std::endl;
	std::cout << "b: " << b << std::endl;
	std::cout << "counter: " << n << std::endl << std::endl;
	return 0;
}

int bissec_converg(double a, double b) {
	int n = 0;
	double m1, m = (a + b) / 2;;
	while (std::abs(b - a) > 0.000001)
	{
		m1 = m;
		m = (a + b) / 2;
		if (f(a) * f(m) < 0)
		{
			b = m;
		}
		else
		{
			a = m;
		}
		n++;
	}
	std::cout << "a: " << a << std::endl;
	std::cout << "b: " << b << std::endl;
	std::cout << "counter: " << n << std::endl << std::endl;
	return 0;
}

int corda_absolutstop(double a, double b) {
	int counter = 0;
	double m;
	while (std::abs(b - a) > 0.000001)
	{
		m = (a * f(b) - b * f(a)) / (f(b) - f(a));
		if (f(a) * f(m) < 0)
		{
			b = m;
		}
		else
		{
			a = m;
		}
		counter++;
		if (counter > 100) break;
	}
	std::cout << "a: " << a << std::endl;
	std::cout << "b: " << b << std::endl;
	std::cout << "counter: " << counter << std::endl << std::endl;
	return 0;
}

int corda_nullfunction(double a, double b) {
	int counter = 0;
	double m;
	while (std::abs(f(b) - f(a)) > 0.000001)
	{
		m = (a * f(b) - b * f(a)) / (f(b) - f(a));
		if (f(a) * f(m) < 0)
		{
			b = m;
		}
		else
		{
			a = m;
		}
		counter++;
		if (counter > 100) break;
	}
	std::cout << "a: " << a << std::endl;
	std::cout << "b: " << b << std::endl;
	std::cout << "counter: " << counter << std::endl << std::endl;
	return 0;
}

int corda_converg(double a, double b) {
	int counter = 0;
	double m1, m = (a * f(b) - b * f(a)) / (f(b) - f(a));;
	while (std::abs(b - a) > 0.000001)
	{
		m1 = m;
		m = (a * f(b) - b * f(a)) / (f(b) - f(a));
		if (f(a) * f(m) < 0)
		{
			b = m;
		}
		else
		{
			a = m;
		}
		counter++;
		if (counter > 100) break;
	}
	std::cout << "a: " << a << std::endl;
	std::cout << "b: " << b << std::endl;
	std::cout << "counter: " << counter << std::endl << std::endl;
	return 0;
}

int main() {
	//f1
	bissec_absolutstop(0.01, 1.00);
	bissec_nullfunction(0.01, 1.00);
	bissec_converg(0.01, 1.00);
	corda_absolutstop(0.01, 1.00);
	corda_nullfunction(0.01, 1.00);
	corda_converg(0.01, 1.00);

	bissec_absolutstop(9.0, 10.00);
	bissec_nullfunction(9.0, 10.00);
	bissec_converg(9.0, 10.00);
	corda_absolutstop(9.0, 10.00);
	corda_nullfunction(9.0, 10.00);
	corda_converg(9.0, 10.00);


	//f2
	/*
	bissec_absolutstop(0.01, 1.00);
	bissec_nullfunction(0.01, 1.00);
	bissec_converg(0.01, 1.00);
	corda_absolutstop(0.01, 1.00);
	corda_nullfunction(0.01, 1.00);
	corda_converg(0.01, 1.00);

	bissec_absolutstop(98.0, 100.00);
	bissec_nullfunction(98.0, 100.00);
	bissec_converg(98.0, 100.00);
	corda_absolutstop(98.0, 100.00);
	corda_nullfunction(98.0, 100.00);
	corda_converg(98.0, 100.00);
	*/

	//f3
	/*
	bissec_absolutstop(0.5, 1.5);
	bissec_nullfunction(0.5, 1.5);
	bissec_converg(0.5, 1.5);
	corda_absolutstop(0.5, 1.5);
	corda_nullfunction(0.5, 1.5);
	corda_converg(0.5, 1.5);
	*/

	
}