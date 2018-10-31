sl= 1
h = 0.1
ni = sl/h
t=c(1:ni)
t[1]=0
x = vector(length=ni)
y = vector(length=ni)

y[1] = 1


fx = function(x,y){
  return(y-x^2)
}

for (i in 1:ni){
  #dx/dt
  k1 = h*fx(x[i],y[i])
  k2 = h*fx(x[i]+(h/2),y[i]+(k1/2))
  k3 = h*fx(x[i]+(h/2),y[i]+(k2/2))
  k4 = h*fx(x[i]+h,y[i]+k3)
  y[i+1] = y[i] + (1/6*(k1+(2*k2)+(2*k3)+k4))
  
  x[i+1] = i*h
}

