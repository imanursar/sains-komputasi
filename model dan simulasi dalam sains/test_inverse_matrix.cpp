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
	double np[99][2];
	double AA[2];
	double A_1[2][2];
	np[0][0] = 1;
	np[0][1] = 0;
	
	 
	double A[2][2] = {{2,5},
					  {1,3}};
	
	double AB[2] = {1,0};
	
	
	double det = (A[0][0]*A[1][1])-(A[0][1]*A[1][0]);
	
    A_1[0][0] = A[1][1]/det;
    A_1[0][1] = -A[0][1]/det;
    A_1[1][0] = -A[1][0]/det;
    A_1[1][1] = A[0][0]/det;
		
	cout << '\n';
	cout << "det " << det << '\n';

	for(int i = 0; i < 2; ++i){
        	for(int k = 0; k < 2; ++k){
    			AA[i] += A[i][k] * AB[k];
		}	
    }
	
	for(int x=0;x<2;x++){
            cout<<AA[x]<<"  ";
    cout<<endl;
    }

}
