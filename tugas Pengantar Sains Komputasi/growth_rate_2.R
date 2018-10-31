sl= 100
r = 0.1
dt = 0.1
ni = sl/dt
p = vector(length=ni)
p[1] = 20
ti=c(1:ni)
ti[1]=0
M=1000

for (i in 1:ni){
 p[i+1] = p[i] + (r*p[i])*dt - (r*p[i]/M)*p[i]*dt
  ti[i+1] = i*dt
}

plot(ti,p,type = "l",cex=1.5)