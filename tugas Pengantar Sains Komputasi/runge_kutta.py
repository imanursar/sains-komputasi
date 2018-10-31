import numpy as np
import matplotlib
import matplotlib.pyplot as plt

sl= 1.1
h = 0.1
ni = sl/h
# t=c(1:ni)
# t[1]=0
x = np.zeros((int(ni+1)))
y = np.zeros((int(ni+1)))

y[0] = 1
x[0] = 0


def fx(x,y):
  return((5*x**2-y)/(np.exp(x+y)))


for i in range (0,int(ni)):
    k1 = h*fx(x[i],y[i])
    k2 = h*fx(x[i]+(h/2),y[i]+(k1/2))
    k3 = h*fx(x[i]+(h/2),y[i]+(k2/2))
    k4 = h*fx(x[i]+h,y[i]+k3)
    y[i+1] = y[i] + (1/6*(k1+(2*k2)+(2*k3)+k4))
    x[i+1] = x[i]+h

for j in range (0,int(ni)):
    print(np.round(x[j],4),end='')
    print("\t|\t",end='')
    print(np.round(y[j],4))

fig, ax1 = plt.subplots()
ax1.plot(x,y,'b-')

ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.grid()
plt.show()
