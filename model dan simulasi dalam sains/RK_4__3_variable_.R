sl= 100
h = 0.001
ni = sl/h
t = vector(length=ni)
t[1]=0
x = vector(length=ni)
y = vector(length=ni)
z = vector(length=ni)
x[1] = 1
y[1] = 1
z[1] = 1


g = 10
rho = 28
b = 8/3

#dx = g*(y-x)*dt
#dy = rho*x - y - x*z
#dz = x*y - b*z

fx = function(t,x,y,z){
  return(g*(y-x))
}

fy = function(t,x,y,z){
  return(rho*x - y - x*z)
}

fz = function(t,x,y,z){
  return(x*y - b*z)
}


for (i in 1:ni){
  #dx/dt
  #k1 = h*f(t,x,y,z)
  #k2 = h*f(t+(h/2),x+(k1/2),y+(k1/2),z+(k1/2))
  #k3 = h*f(t+(h/2),x+(k2/2),y+(k2/2),z+(k2/2))
  #k4 = h*f(t+h,x+k3,y+k3,z+k3)
  #x[i+1] = x[i] + (1/6*(k1+(2*k2)+(2*k3)+k4))
  
  #dx/dt
  kx1 = h*fx(t[i],x[i],y[i],z[i])
  ky1 = h*fy(t[i],x[i],y[i],z[i])
  kz1 = h*fz(t[i],x[i],y[i],z[i])
  
  kx2 = h*fx(t[i]+(h/2),x[i]+(kx1/2),y[i]+(ky1/2),z[i]+(kz1/2))
  ky2 = h*fy(t[i]+(h/2),x[i]+(kx1/2),y[i]+(ky1/2),z[i]+(kz1/2))
  kz2 = h*fz(t[i]+(h/2),x[i]+(kx1/2),y[i]+(ky1/2),z[i]+(kz1/2))
  
  kx3 = h*fx(t[i]+(h/2),x[i]+(kx2/2),y[i]+(ky2/2),z[i]+(kz2/2))
  ky3 = h*fy(t[i]+(h/2),x[i]+(kx2/2),y[i]+(ky2/2),z[i]+(kz2/2))
  kz3 = h*fz(t[i]+(h/2),x[i]+(kx2/2),y[i]+(ky2/2),z[i]+(kz2/2))
  
  kx4 = h*fx(t[i]+h,x[i]+kx3,y[i]+ky3,z[i]+kz3)
  ky4 = h*fy(t[i]+h,x[i]+kx3,y[i]+ky3,z[i]+kz3)
  kz4 = h*fz(t[i]+h,x[i]+kx3,y[i]+ky3,z[i]+kz3)
  
  x[i+1] = x[i] + (1/6*(kx1+(2*kx2)+(2*kx3)+kx4))
  y[i+1] = y[i] + (1/6*(ky1+(2*ky2)+(2*ky3)+ky4))
  z[i+1] = z[i] + (1/6*(kz1+(2*kz2)+(2*kz3)+kz4))
  
  t[i+1] = i*h
}

library(rgl)
plot3d(x, y, z, col="red", size=3, type = "l")