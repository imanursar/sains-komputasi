#include <chrono>
#include <random>
#include <iostream>

using namespace std;

double gxyz(double x,double y,double z){
double d = (3*x*y*pow(z,2))-(2*x*pow(y,2)*z)+(pow(x,2)*y*z);
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
	double n_max= 1000000;
	double n_hit = 0;
	double integral=0;
	double x;
	double y;
	double z;
	double g;
	int result_1[5]; 
	double result[5][2];
	
	
	// construct a trivial random generator engine from a time-based seed:
	unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
  	std::default_random_engine generator (seed);
	std::uniform_real_distribution<double> distribution (0.0,1.0);

  	for (int i=0; i<n_max; ++i){
    	x = min_x + (distribution(generator))*(max_x-min_x);
    	y = min_y + (distribution(generator))*(max_y-min_y);
    	z = min_z + (distribution(generator))*(max_z-min_z);
    	g = (distribution(generator))*max_g;
		//cout << x << " " << y;
    	//cout << endl;
			
    	if (g < gxyz(x,y,z)) {
  			n_hit = n_hit + 1;
  			//cout << g << "		" << gxyz(x,y,z) << "		" << n_hit;
  			//cout << endl; 
		}
	}
	cout << '\n';
	cout << "nilai n_hit adalah " << n_hit << '\n';
	cout << "nilai n_max adalah " << n_max << '\n';
	cout << "nilai integralnya adalah " << jumlah(n_hit,n_max,max_x,min_x,max_y,min_y,max_z,min_z,max_g);
  	cout << endl;
	return 0;
}
