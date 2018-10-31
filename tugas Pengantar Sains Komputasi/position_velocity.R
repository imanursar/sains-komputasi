sl = 4
dt = 0.1
ni = sl/dt
a = -9.81
v = vector(length=ni)
r = vector(length=ni)
v[1] = 15
r[1] = 11
ti=c(0:ni)

for (i in 1:ni){
  v[i+1] = v[i] + a*dt
  r[i+1] = r[i] + v[i+1]*dt
}

plot(ti,r,type = "l",lwd=2,col="blue",xlab = "time(Hour)",ylim = c(-15,25))
points(ti,v,type = "l",lwd=1.5,col="red")
abline(h=0)
legend(-1,-2,c("velocity","position"),col=c("blue","red"),text.col = c("blue","red"), lwd = c(2,1), bg = "gray90")