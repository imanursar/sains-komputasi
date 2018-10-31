import numpy as np

S = np.ones((10,10))*999
# second_col = matrix[:,1,:]
S[0,1]=3
S[0,2]=5
S[0,5]=2
S[1,2]=6
S[1,3]=2
S[2,1]=6
S[2,3]=4
S[2,4]=4
S[2,5]=3
S[3,2]=4
S[3,4]=1
S[3,9]=3
S[4,3]=1
S[4,7]=3
S[5,2]=2
S[5,6]=2
S[6,4]=1
S[6,5]=1
S[6,7]=3
S[7,6]=2
S[7,8]=1
S[7,9]=1
S[8,7]=3
S[8,9]=3
S[9,4]=2

print(S)

n=len(S)
v=1
dest=n #destination node
cost=S #distance matrix

def dijkstra(n,v,cost,dest):
    dest = np.zeros((n))
    flag = np.zeros((n))
    prev = np.zeros((n))

    for i in range(0,n):
        prev[i] = -1
        dest[i] = cost[v-1,i]

    count = 1

    while (count <=n):
        min = 999

        for w in range(0,n):
            if (dest[w] < min and not flag[w]):
                min = dest[w]
                u = w

        flag[u] = 1
        count = count+1

        for w in range(0,n):
            if ((dest[u]+cost[u,w] < dest[w]) and not flag[w]):
                dest[w] = dest[u]+cost[u,w]
                prev[w] = u

        # print(prev)
    return(prev)

def savepath(f,x):
    path = []
    path.append(int(x)+1)
    while (f[int(x)] != -1):
        path.append(int(f[int(x)])+1)
        x = f[int(x)]
        savepath(f,x)

    path.append(1)
    return(path)

prev = dijkstra(n,v,cost,dest)
print(prev)

path = savepath(prev,dest-1)
print(path)
