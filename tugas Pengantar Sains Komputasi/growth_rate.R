sl = 50
gr = 0.1
dt = 0.1
ni = sl/dt
p = vector(length=ni)
p[1] = 100
ti=c(1:ni)
ti[1]=0

  for (i in 1:ni){
    gr1 = gr*p[i]
    p[i+1] = p[i] + gr1*dt
    ti[i+1] = i*dt
  }

plot(ti,p,type = "l",cex=1.5)