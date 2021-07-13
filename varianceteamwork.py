def input():
    return next(input_data)

def sim_input():
    with (open("varianceteamwork.txt", "r")) as f:
        rows=f.readlines()
    for row in rows:
        yield row.rstrip()

input_data=sim_input()

####################
I=input
N=int(I())
M=int(I())
V=999
for t in range(N):
 w=[*map(int,I().split())]
 x=sum(w)/M
 v=sum(list(map(lambda d:(d-x)**2,w)))/M
 if v<V:V=v;T=t+1
print(T)


#from statistics import *
#I=input
#n=int(I())
#m=int(I())
#g=[map(int,I().split())for i in range(n)]
#print(min((variance(g[i]),i+1)for i in range(n))[1])

