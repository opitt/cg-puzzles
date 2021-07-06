#remove odd/even characters, dont keep double spaces
t=input().split()
for i,w in enumerate(t):t[i]="".join([("",c)[ord(c)%2==i%2] for c in w])
print(" ".join(w for w in t if w!= ""))
