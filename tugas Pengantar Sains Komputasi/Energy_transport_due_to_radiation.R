#Energy transport due to radiation

#dT/dr = -3*k*p*L/4*a*c*T^3*4*phi*r^2

ni = 82
k = 0.1
p = 1410
L = 3.84e26
#c = 299792458
rho = 5.67e-8
#a = 7.56e-16
dr = 6960
T = vector(length=ni)
#dT = vector(length=ni)
T[1] = 1.6e7
r = vector(length=ni)
dT = vector(length=ni)
rr = 696000

for (i in 1:ni){
  #T[i+1] = T[i] + (-3*k*p*L*dr)/(4*a*c*(T[i]^3)*4*pi*(r[i])^2)
  dT[i] = ((-3*k*p*L*dr)/(64*pi*rho*(rr^2)*(T[i]^3)))
  T[i+1] = T[i] + dT[i]
  r[i+1] = r[i] + dr
}

plot(r,T,type = "l",lwd=2,col="blue",xlab = "Radius")