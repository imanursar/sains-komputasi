#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>

using namespace std;

int main (){
	float v[5]={ 1, 1, 1, 1, 1};
	float y[5];
	float vv[5];
	float T = 0;
	float ee = 0;
	float D[5]={ 0, 0, 0, 0, 0};
	float n = 0.1;
	double wo[5][5];
	double dw[5][5]={ { 0, 0, 0, 0, 0 },
                  { 0, 0, 0, 0, 0 },
                  { 0, 0, 0, 0, 0 },
                  { 0, 0, 0, 0, 0 },
                  { 0, 0, 0, 0, 0 } };
	double w[5][5]={ { 0, 0, 0.3, -0.8, 0 },
                  { 0, 0, 0.5, 0.1, 0 },
                  { 0, 0, 0.2, 0, 0.2 },
                  { 0, 0, 0, -0.2, 0.7 },
                  { 0, 0, 0, 0, 0.3 } };
	
	for(int i=0;i<4;i++){
		vv[i]=0;
		for (int j=0;j<4;j++){
		vv[i] = vv[i]+(w[j][i]*v[j]);
		}
	}
	
	for(int i=0;i<4;i++){
		y[i] = 1/(1+exp(-vv[i]));
	}
	
	for(int i=4;i<5;i++){
		vv[i] = 0;
		for (int j=2;j<4;j++){
			vv[i] = vv[i]+(y[j]*w[j][i]);
		}
		vv[i] = vv[i] + w[i][i];
		y[i] =  1/(1+exp(-vv[i]));
	}
	
	ee = T - y[4];
	
	D[4] = y[4]*(1-y[4])*ee;
	for (int i=3;i>1;i--){	
		D[i] = y[i]*(1-y[i])*D[4]*w[i][4];
	}
	
	dw[4][4] = n*D[4];
	for (int i=4;i>1;i--){
		dw[i][i] = n*D[i];		
	}
	
	for (int i=3;i>1;i--){
		dw[i][4] = n*y[i]*D[4];
		for (int j=i-1;j>=0;j--){
			dw[j][i] = n*v[j]*D[i];
		}
	}
	
	
	for (int i=0; i < 5; ++i){
		for (int j=0; j < 5; ++j){
			wo[i][j] = w[i][j] + dw[i][j];
		}
	}
	
//-----------------------------------------------------------------------------------------------------------------------------//	
	cout << "w";cout << endl;
	for (int i=0; i < 5; ++i){
		for (int j=0; j < 5; ++j){
			cout << w[i][j] << "		";
		}
		cout << endl;
	}
	
	cout << "------------------------------------------";
	cout << endl;
	
	cout << "dw";cout << endl;
	for (int i=0; i < 5; ++i){
		for (int j=0; j < 5; ++j){
			cout << dw[i][j] << "		";
		}
		cout << endl;
	}
	
	cout << "------------------------------------------";
	cout << endl;
	
	cout << "wo";cout << endl;
	for (int i=0; i < 5; ++i){
		for (int j=0; j < 5; ++j){
			cout << wo[i][j] << "		";
		}
		cout << endl;
	}
	cout << "------------------------------------------";
	cout << endl;
	
	cout << "y";cout << endl;
	for (int j=0; j < 5; ++j){
		cout << y[j] << " ";
		cout << endl;
	}
	
	cout << "------------------------------------------";
	cout << endl;
	
	//cout << "------------------------------------------";
	//cout << endl;
	
	cout << "D";cout << endl;
	for (int j=0; j < 5; ++j){
		cout << D[j] << " ";
		cout << endl;
	}
	
	cout << "------------------------------------------";
	cout << endl;
	
	cout << "ee";cout << endl;
	cout << ee << " ";
		cout << endl;
    
	return 0;	
}
