i=input
I=int
for _ in range(I(i())):t=i();print(str(sum(map(I,t[:3]))==sum(map(I,t[-3:]))).lower())
