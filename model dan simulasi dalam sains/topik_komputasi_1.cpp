#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>

using namespace std;

double gx(double k,double dp, double R, double h,double x){
	double delta = (dp*pow(R,3)*h)/(pow(pow(x,2)+pow(h,2),1.5));
	return delta;
} 

int main (){
	
	ofstream file_objek;
	file_objek.open("data_1.txt");
	
	double k = 1;
	double dp = 2;
	double x0 = -100;
	double x1 = 100;
	double R = 100;
	double h = 10;
	
	double x[9999];
	x[0]=x0;
	double g[9999];
	
	
	for (int i=0;i<(x1-x0);i++){
		x[i] = x0 + i;
		g[i] = gx(k,dp,R,h,x[i]);
		file_objek<<x[i]<<"	"<<g[i]<<endl;
	}
	
	file_objek.close();
	return 0;
}

