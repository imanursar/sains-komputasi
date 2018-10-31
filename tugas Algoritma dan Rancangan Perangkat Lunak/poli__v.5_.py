# library ======================================================================
import math
import numpy as np
from matplotlib.figure import Figure
from numpy import arange
import matplotlib.pyplot as plt
from multiprocessing import Process
from matplotlib.pyplot import plot, show

#function ======================================================================

#print hasil turunan dari dari fungsi polinomial input

def different(lst):
    lst_1 = []
    print("\nbentuk turunan dari polinomial diatas adalah: ")
    j = len(lst) - 1
    for i in range(0,len(lst)-2):
        lst_1.append(lst[i]*j)
        print(repr(lst[i]*j) + "x^" + repr(j-1) + " +", end=" ")
        j = j - 1

    print(repr(lst[i+1]))
    lst_1.append(lst[i+1])
    return(lst_1)

def fx(lst,x):
    sum1=0
    jj= len(lst) - 1
    for i in range(0,len(lst) - 1):
        while(jj>0):
            sum1 = sum1 + lst[i] * np.power(x,jj)
            break
        jj=jj-1
    sum1 = sum1 + lst[len(lst) - 1]
    # print("\nThe value of the polynomial is:",sum1)
    return (sum1)

def fxx(lst,x):
    sum2 = 0
    j=len(lst) - 1
    for i in range(0,len(lst) - 1):
        while(j>0):
            sum2 = sum2 + lst[i] * np.power(x,j)
            break
        j=j-1
    sum2 = sum2 + lst[len(lst) - 1]
    # print("The value of the differential is:",sum2,"\n")
    return (sum2)

def newton_raphson(init,acc,lst):
    n = 0
    x1 = init
    x2 = 0
    f1 = fx(lst,init)
    f2 = fxx(lst_1,init)

    # while (abs(x1 - x2) > 0.00001):
    for i in range(0,20):
        x2 = x1 - f1/f2
        # print(np.around(f1/f2,decimals=6))
        print("error: " + str(abs(x1 - x2)))
        print ("x1 =\t" + str(np.around(x1,decimals=6)) + "\t| x2 =\t" + str(np.around(x2,decimals=6)))
        if (abs(x1 - x2) > acc):
            x1 = x2
            f1 = fx(lst,x1)
            f2 = fxx(lst_1,x1)
            n = n + 1
        else:
            break

    return(np.around(x2,decimals=6))



# f(x) =========================================================================
print("masukkan nilai koefisien polinomial (contoh: ax^3 + bx^2 + cx + d ===> a b c d)")
print("nilai koefisien dari turunannya akan dihitung secara manual")
lst=[]

a=input("\nnilai koefisien polinomial:")
a = a.split(' ')
lst = [int(i) for i in a]

print("\nbentuk polinomialnya adalah: ")
j = len(lst) - 1
for i in range(0,len(lst)-1):
    print(repr(lst[i]) + "x^" + repr(j) + " +", end=" ")
    j = j - 1

print(repr(lst[i+1]))

# f'(x) =========================================================================

lst_1 = different(lst)

# plot figure ==================================================================
inter=[]
print("\n"+"masukkan nilai interval ")
aa = input("\ninterval:")
aa = aa.split(' ')
inter = [float(i) for i in aa]

t = arange(inter[0], inter[1], 0.1)

s = fx(lst,t)
ss = fxx(lst_1,t)

# for i in range(0,len(t)):
#     print(str(np.around(t[i],decimals=2)) +" | "+ str(np.around(s[i],decimals=2))+" | "+ str(np.around(ss[i],decimals=2)))

fig = plt.figure()
axx = plt.subplot(111)
axx.plot(t, s, lw=2)

ax = plt.gca()  # gca stands for 'get current axis'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
axx.plot(t, s, color="blue", linewidth=2.5, linestyle="-", label="Polinomial")
axx.plot(t, ss, color="red",  linewidth=2.5, linestyle="-", label="Differential")

axx.legend(loc='upper left')

plt.pause(2)

# interval 1 =========================================================================
# print("\n"+"Enter initial number for interval -10 < x < 0")
# a_in=float(input("Initial number:"))
#
# while (-10 > a_in or a_in > 0):
#     print("\n"+"Enter initial number for interval -10 < x < 0")
#     a_in=float(input("Initial number:"))

# # interval 2 =========================================================================
# print("\n"+"Enter initial number for interval 0 < x < 2")
# b_in=float(input("Initial number:"))
#
# while (0 > b_in or b_in > 2):
#     print("\n"+"Enter initial number for interval 0 < x < 2")
#     b_in=float(input("Initial number:"))
#
# # tebakan awal =========================================================================
print("\n"+"masukkan nilai tebakan awal (contoh: 1 2 3)")
print("pastikan banyaknya tebakan sama dengan jumlah akar-akar yang dapat dilihat pada gambar dan berada pada interval yang diinput")
c_in=[]

a=input("\nnilai tebakan awal:")
a = a.split(' ')
c_in = [float(i) for i in a]

# akurasi =========================================================================

print("\n"+"masukkan nilai akurasi")
e=float(input("akurasi:"))
print("\n")

################################################################################

root = []

for i in range(0,len(c_in)):
    print("nilai inisial awal: " + repr(c_in[i]))
    root.append(newton_raphson(c_in[i],e,lst))
    print("\n\n")

# fx = newton_raphson(c_in,e,lst)
print("nilai akar akar dari polinomial diatas adalah: ")
print(root)

## lokal minimun dan maksimum =============================================================================

print("nilai lokal minimum dan maksimum yang terdeteksi ada pada: \n")

if (s[0] > 0):
    print("nilai lokal maksimum dapat berada pada titik ujung interval: x = " + str(t[0]))
if (s[0] < 0):
    print("nilai lokal minimum dapat berada pada titik ujung interval: x = " + str(t[0]))

if (s[len(s)-1] > 0):
    print("nilai lokal maksimum dapat berada pada titik ujung interval: x = " + str(np.around(t[len(s)-1],decimals=2)))
if (s[len(s)-1] < 0):
    print("nilai lokal minimum dapat berada pada titik ujung interval: x = " + str(np.around(t[len(s)-1],decimals=2)))

deriv = []
func = []
pos = []
for i in range(1,len(ss)-1):
    if (ss[i] == 0):
        print("\nnilai lokal minimum dan maksimum berada pada x = ", s[i])
    elif((ss[i-1] > 0 and ss[i+1]<0) or (ss[i-1]<0 and ss[i+1] > 0)):
        if ((abs(ss[i]) < abs(ss[i+1])) and (abs(ss[i]) < abs(ss[i-1]))):
            deriv.append(np.around(ss[i-1],decimals=2))
            deriv.append(np.around(ss[i+1],decimals=2))
            pos.append(np.around(t[i-1],decimals=2))
            pos.append(np.around(t[i+1],decimals=2))
            func.append(np.around(s[i-1],decimals=2))
            func.append(np.around(s[i+1],decimals=2))
            if (ss[i-1]>ss[i+1]):
                print("nilai lokal maksimum berada pada rentang "+ "| x1 = " + str(np.around(t[i-1],decimals=2)) + " dan x2 = " + str(np.around(t[i+1],decimals=2)) + " |")
            else:
                print("nilai lokal minimum berada pada rentang "+ "| x1 = " + str(np.around(t[i-1],decimals=2)) + " dan x2 = " + str(np.around(t[i+1],decimals=2)) + " |")
