#Input is a number, n.
#If n is 3, the output is:
#321
#12
#1
#If n is 5, the output is:
#12345
#4321
#123
#21
#1

#120 characters
p=lambda *r:"".join(map(str,range(*r)))
l=1
for n in range(int(input()),0,-1):print((p(n,0,-1),p(1,n+1,1))[l%2!=0]);l+=1
