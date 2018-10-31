#include <iostream>
#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <cmath>


using namespace std;

double bernoulli(double Pa,double Pb, double rho, double g, double ha, double hb, double Va){
	double Vb = pow(2*((Pa - Pb) + rho*g*(ha-hb) + (0.5*rho*pow(Va,2)))/rho,0.5);
	return Vb;
} 

double dv(double v, double H, double dt, double e, double A, double G){
	double d = v + H*dt - (e*v/A)*dt-G*dt;
	return d;
} 

double dv2(double v, double H, double dt, double e, double A, double G,double G1){
	double d = v + H*dt +G*dt - (e*v/A)*dt-G1*dt ;
	return d;
}

double dl(double k,double A,double P2,double P1,double mu,double L){
	double d = k*A*(P2 - P1)/mu*L;
	return d;
} 

int main (){
	double e[4]= {0.1,0.1,0.1,0.1};
	double A[4] = {150,100,200,300}; //180,120,200,661	km^2
	double V[999][4];
	double V[0][] = {100,100,100,100}; 
	double H[4] = {30,45,35,40}; //323,442,353,402
	double G[4] = {100,100,100,100}; //cilember, bogor, depok, jakarta mm/bulan januari
	double h[4] = {40,20,10,25}; // 800,265,100,25 m
	double P[4] = {1,1,1,1};
	double dt = 1;
	double g = 10;
	double rho = 1;
	
	for (int i=0; i<10; ++i){
		for (int j=0; j<2; ++j){		
			if (j==0) {
				cout << "nilai V_1 " << V[i]<<'\n';
				V[i][j] = V[][j] + dv(V[j],H[j],dt,e[j],A[j],G[j]);
				cout << "nilai V_2 " << V[i] << " + " << dv(V[i],H[i],dt,e[i],A[i],G[i]) <<'\n';
				//cout << "nilai V" << j+1 << "  "<< i <<" adalah " << V[i] << "  delta V adalah " << dv(V[i],H[i],dt,e[i],A[i],G[i]) <<'\n';
			}
			
			else {
				V[j+1] = V[j] + dv2(V[j],H[j],dt,e[j],A[j],G[j],G[j+1]);
				cout << "nilai V" << j+1 << "  "<< i <<" adalah " << V[i] << "  delta V adalah " << dv2(V[i],H[i],dt,e[i],A[i],G[i],G[i+1]) << '\n';
				cout << '\n';
			}
		}
		
		//else {
		//	V[i] = V[i] + dv2(H[i],G[i],e,V[i],A[i],G[i+1],dt);
		//	cout << '\n';
		//	cout << "nilai V" << i+1 << " adalah " << V[i] << '\n';
		//}
		
		
	}
return 0;
}
