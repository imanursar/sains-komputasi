#include <chrono>
#include <random>
#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <cmath>
#include <stdlib.h>

using namespace std;

double gxyz(double x,double y,double z){
double d = (3*x*y*pow(z,2))-(2*x*pow(y,2)*z)+(pow(x,2)*y*z);
	return d;
}

double gg(double x,double y,double z){
double d = ((0.25*pow(x,2)*pow(y,2)*pow(z,3))-((0.1666666)*pow(x,2)*pow(y,3)*pow(z,2))+(0.08333*pow(x,3)*pow(y,2)*pow(z,2)));
	return d;
} 

double jumlah(double n_hit,double n_max,double max_x,double min_x,double max_y,double min_y,double max_z,double min_z,double max_g){
double q = (n_hit/n_max)*(max_x-min_x)*(max_y-min_y)*(max_z-min_z)*max_g;
	return q;
}

int main (){
	int min_x = 0;
	int max_x = 3;
	int min_y = 1;
	int max_y = 4;
	int min_z = 1;
	int max_z = 5;
	int max_g = 1000;
	double n_max = 1000000;
	double n_hit = 0;
	double integral=0;
	double x;
	double y;
	double z;
	double g;
	int j =99;
	
	
	cout << '\n';
	cout << setw(40) << "   nilai iterasi maksimum= " << n_max;
	cout << '\n';
	cout << setw(40) << "   nilai integral= " << 2727;
	cout << '\n';
	cout << setw(40) << "   nilai fungsi maksimum= " << max_g;
	cout << '\n';
	cout << "===========================================================";
	cout << endl;
	
	// construct a trivial random generator engine from a time-based seed:
	unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
  	std::default_random_engine generator (seed);
	std::uniform_real_distribution<double> distribution (0.0,1.0);
	
	cout <<setw(8) << "jumlah iterasi" << setw(20) << "jumlah hit" << setw(20) << "nilai integral"<< setw(15) << "error (%)";
	
  	for (int i=0; i<n_max; ++i){
    	x = min_x + (distribution(generator))*(max_x-min_x);
    	y = min_y + (distribution(generator))*(max_y-min_y);
    	z = min_z + (distribution(generator))*(max_z-min_z);
    	g = (distribution(generator))*max_g;
			
    	if (g < gxyz(x,y,z)) {
  			n_hit = n_hit + 1;
  		}
		if (i==j) {
  			cout << '\n';
		  	cout <<setw(8) << i+1 << setw(20) << n_hit/3 << setw(20) << jumlah(n_hit,i+1,max_x,min_x,max_y,min_y,max_z,min_z,max_g) << setw(20) << 100*(abs(jumlah(n_hit,i+1,max_x,min_x,max_y,min_y,max_z,min_z,max_g)-2727)/2727);
		  	//<< setw(20) << 100*(abs(jumlah(n_hit,i,max_x,min_x,max_y)-(ix(max_x)-ix(min_x)))/(ix(max_x)-ix(min_x)));
		  	j = (j*10)+9;
		}
	}
	return 0;
}
