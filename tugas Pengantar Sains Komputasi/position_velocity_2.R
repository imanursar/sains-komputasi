n =150
dt = 0.1
m = 0.5
g = -9.81
rr = 0.05
w = m*g
D = pi*rr^2
v = vector(length=n)
r = vector(length=n)
vv = vector(length=n)
ti = vector(length=n)
v[1] = 0
r[1] = 400
ti[1] = 0

for(i in 1:n){
  af = -0.65*D*v[i]*(abs(v[i]))
  tf = w + af
  a = tf/m
  v[i+1] = v[i] + a*dt
  r[i+1] = r[i] + v[i]*dt
  ti[i+1] = ti[i] + dt
  
}

### add extra space to right margin of plot within frame
par(mar=c(5, 4, 4, 6) + 0.1)

plot(ti,abs(v),type = "l",lwd=2,col="blue",xlab = "time(Hour)",log = "y",xaxt="n")
box()
#plot(ti,r,type = "l",lwd=1.5,col="red")

par(new=TRUE)

plot(ti, r, axes=F, xlab=NA, ylab=NA,"l",lwd=1.5,col="red",xaxt="n")
axis(side = 4)
minor.ticks.axis(1,9,mn=0,mx=15)
#mtext(side = 4, line = 3, 'Number genes selected')
#legend("topleft",legend=c(expression(-log[10](italic(p))), "N genes"),lty=c(1,0), pch=c(NA, 16), col=c("red3", "black"))
