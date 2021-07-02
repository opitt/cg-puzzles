a = input()
b = input()
res=""
for i in range(len(a)):
    for j in range(len(a)-i+1):
        if a[i:i+j+1] in b and len(res)<j:
            res=a[i:i+j+1]
res=res if len(res) else "NONE"
print(res)
