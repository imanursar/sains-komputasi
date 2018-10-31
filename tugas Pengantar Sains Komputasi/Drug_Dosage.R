sl = 8
gr = 0.1
dt = 0.1
ni = sl/dt
q = vector(length=ni)
q[1] = 217
ti=c(1:ni)
ti[1]=0
tt=3.2 #jam

for (i in 1:ni){
  k = -log(0.5)/tt
  q[i+1] = q[i] - q[i]*k*dt
  ti[i+1] = i*dt
}

plot(ti,q,type = "l",cex=1.5)