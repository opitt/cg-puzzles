import string as s
p=input()
c=lambda m:len([c for c in p if c in m])
a=c(s.ascii_lowercase)
A=c(s.ascii_uppercase)
d=c(s.digits)
L=c(p)
s=c(" ")
print(str(8<=L<=15 and d and A and s<1)+",",A*10+a*5+d+(L-s-A-a-d)*25)
