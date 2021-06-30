#can the given word be written with only letters from one of the given keyboard rows


#162 chars
w=input()
k=["`1234567890-=","qwertyuiop[]\\","asdfghjkl;'","zxcvbnm,./"]
l=lambda i:all(map(lambda c:c in k[i],w))
print(("No","Yes")[l(0)or l(1)or l(2)or l(3)])


#q=['`1234567890-=','qwertyuiop[]\\',"asdfghjkl;'",'zxcvbnm,./']
#z=input()
#print(['No','Yes'][max(all(x in w for x in z)for w in q)])
