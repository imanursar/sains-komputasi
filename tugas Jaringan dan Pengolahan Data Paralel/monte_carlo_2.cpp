#include <chrono>
#include <random>
#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <cmath>
#include <stdlib.h>

using namespace std;

double dx(double x){
	double d = 5*(pow(x,3))-3*(pow(x,2))+x-7;
	return d;
} 

double ix(double x){
	double d = (1.25*pow(x,4))-(pow(x,3))+(0.5*pow(x,2))-7*x;
	return d;
}

double jumlah(double n_hit,double n_max,double max_x,double min_x,double max_y){
double q = (n_hit/n_max)*(max_x-min_x)*max_y;
	return q;
}


int main (){
	double min_x = 1;
	double max_x = 5;
	double max_y = 1000;
	double n_max = 1000000;
	double n_hit = 0;
	double integral=0;
	double x;
	double y;
	int j =99;
	
	cout << '\n';
	cout << setw(40) << "   nilai iterasi maksimum= " << n_max;
	cout << '\n';
	cout << setw(40) << "   nilai integral= " << ix(max_x)-ix(min_x);
	cout << '\n';
	cout << setw(40) << "   nilai fungsi maksimum= " << max_y;
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
    	y = (distribution(generator))*max_y;
			
    	if (y < dx(x)) {
  			n_hit = n_hit + 1;
		}	
		if (i==j) {
  			cout << '\n';
		 	cout <<setw(8) << i+1 << setw(20) << n_hit << setw(20) << jumlah(n_hit,i,max_x,min_x,max_y) << setw(20) << 100*(abs(jumlah(n_hit,i,max_x,min_x,max_y)-(ix(max_x)-ix(min_x)))/(ix(max_x)-ix(min_x)));
		  	j = (j*10)+9;
		}
	}
	return 0;
}
