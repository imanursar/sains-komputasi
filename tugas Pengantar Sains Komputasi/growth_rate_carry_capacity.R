sl= 100
r = 0.1
dt = 0.1
ni = sl/dt
p = vector(length=ni)
p[1] = 20
ti=c(1:ni)
ti[1]=0
M= vector(length=ni)
M[1] = 100
M[2] = 101
a=0.05

for (i in 3:ni){
  M[i] = M[i-1] + (a*(M[i-1]-M[1])*(1-((M[i-1]-M[1])/M[2])))*dt
  
}
for (i in 1:ni){
  p[i+1] = p[i] + (r*p[i])*dt - (r*p[i]/M[i])*p[i]*dt
  ti[i+1] = i*dt
}

plot(ti,p,type = "l",lwd=2,col="blue",xlab = "time(year)",ylab="Population")
points(ti[1:1000],M,type = "l",lwd=1.5,col="red")
legend(60,80,c("Population","Carrying capacity"),col=c("blue","red"),text.col = c("blue","red"), lwd = c(2,1), bg = "gray90")
