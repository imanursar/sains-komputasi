#include <chrono>
#include <random>
#include <iostream>

using namespace std;

double dx(double x){
	double d = 5*(pow(x,3))-3*(pow(x,2))+x-7;
	return d;
} 

int main (){
	int min = 1;
	int max = 5;
	int max_y = 1000;
	double n_max = 1000;
	double n_hit = 0;
	double integral=0;
	double x;
	double y;
	
	// construct a trivial random generator engine from a time-based seed:
	unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
  	std::default_random_engine generator (seed);
	std::uniform_real_distribution<double> distribution (0.0,1.0);
	//cout << "some random numbers between 0.0 and 100.0: " << std::endl;
  
  	for (int i=0; i<n_max; ++i){
    	x = min + (distribution(generator))*(max-min);
    	y = (distribution(generator))*max_y;
    	//cout << x << " " << y;
    	//cout << endl;
			
    	if (y < dx(x)) {
  			n_hit = n_hit + 1;
  			//cout << y << "		" << dx(x) << "		" << n_hit;
  			//cout << endl;
		}
	}
	integral = (n_hit/n_max)*(max-min)*max_y;
	cout << '\n';
	cout << "nilai n_hit adalah " << n_hit << '\n';
	cout << "nilai integralnya adalah " << integral;
  	cout << endl;
	return 0;
}
