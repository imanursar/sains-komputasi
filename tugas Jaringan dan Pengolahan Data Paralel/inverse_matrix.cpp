#include <iostream>
#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <cmath>


using namespace std;


int main (){
	double a1 = 0.1;
	double a2 = 3;
	double b1 = 5;
	double b2 = 0.2;
	double dt[6] = { 0.001, 0.01, 0.1, 1, 10, 100};
	double np[1000][2];
	np[0][0] = 1;
	np[0][1] = 0;
	double A_1[2][2];
	double AA[2][2];
	
	
	
	double w;
  	cout << "Please enter an w value (w = 0, 0 < w < 1, w = 1):  ";
  	cin >> w;
  	int m;
	cout << "Please enter an dt value(0 = 0.001)"<< '\n';
  	cout << "                        (1 = 0.01 )"<< '\n';
  	cout << "                        (2 = 0.1  )"<< '\n';
  	cout << "                        (3 = 1    )"<< '\n';
  	cout << "                        (4 = 10   )"<< '\n';
  	cout << "                        (5 = 100  )"<< '\n';
  	cout << "                        (6 = 1000 )"<< "=  ";
	cin >> m;
	

	double A[2][2] = {{1-w*dt[m]*a1,-w*dt[m]*b1},
					  {w*dt[m]*a2,1-w*dt[m]*b2}};
		
	double B[2][2] = {{((1-w)*dt[m]*a1)+1,(1-w)*dt[m]*b1},
					  {(1-w)*dt[m]*a2,((1-w)*dt[m]*b2)+1}};
		
		
	double det = (A[0][0]*A[1][1])-(A[0][1]*A[1][0]);
		
	    A_1[0][0] = A[1][1]/det;
   		A_1[0][1] = -A[0][1]/det;
   		A_1[1][0] = -A[1][0]/det;
	   	A_1[1][1] = A[0][0]/det;
    	
    	for(int i = 0; i < 2; ++i){
        	for(int j = 0; j < 2; ++j){
        		for(int k = 0; k < 2; ++k){
    				AA[i][j] += A_1[i][k] * B[k][j];
     			}
			}	
    	}
	
	for(int n=0; n<1000; ++n){
    np[n+1][0] = AA[0][0] * np[n][0] + AA[0][1] * np[n][1];
	np[n+1][1] = AA[1][0] * np[n][0] + AA[1][1] * np[n][1];	
	}

	for (int i=0; i < 1000; ++i){
		for (int j=0; j < 2; ++j){
			cout << np[i][j] << "		";
		}
	cout << endl;
	}
}
