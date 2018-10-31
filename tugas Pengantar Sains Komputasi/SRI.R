sl= 150
dt = 1
tt=c(0:(ni-1))
ni = sl/dt
s = vector(length=ni)
s[1] = 1
i = vector(length=ni)
i[1] = 1.27e-6
r = vector(length=ni)
r[1] = 0
b = 0.5
k = 1/3

for (j in 1:(ni-1)){
  s[j+1] = s[j] - b*s[j]*i[j]*dt
  i[j+1] = i[j] + (b*s[j]*i[j]-k*i[j])*dt
  r[j+1] = r[j] + k*i[j]*dt
  #ti[j+1] = j*dt
}

plot(tt,s,type = "l",lwd=3,lty = 1,col="green",ylim = c(0,1),ylab = "Rasio Populasi", xlab = "waktu(hari)", main = "Perubahan Populasi")
points(tt,i,type = "l",lwd=3,lty = 2,col="blue")
points(tt,r,type = "l",lwd=3,lty = 3,col="red")
legend(3,0.7,c("S(t)","i(t)","R(t)"),col=c("green","blue","red"),text.col = c("green","blue","red"), lwd = c(3,3,3),lty = c(1,2,3), bg = "gray90")
grid(10,NULL, lwd = 1, lty = 1)