expected="""~E
!F
@C
#c
$G
%B
^A
&h
*a
(g
)b
+f
`I
1d
2D
3i
4J
5e
6M
7k
8L
9l
0H
=K
\j
/m
""".splitlines()

def input():
    return next(input_data)

def sim_input():
    with (open("ghost-legs-data.txt", "r")) as f:
        rows=f.readlines()
    for row in rows:
        yield row.rstrip()

input_data=sim_input()

w, h = map(int,input().split())
top_org = input().replace(" ","")
top = top_org
l=len(top_org)
for i in range(h-2):
    line = input()
    line=line.replace("|-","R ").replace("-|"," L").replace(" ","")
    top_next=[""]*l
    for i, td in enumerate(zip(top,line)):
        t,d = td
        top_next[i if d=="|" else i+1 if d=="R" else i-1]=t
    top="".join(top_next)
bottom = input().replace(" ","")

top_to_bottom={k:v for k,v in zip(top,bottom)}
result=[t+top_to_bottom[t] for t in top_org]
print("\n".join(result))

for e,r in zip(expected,result):
    print(e==r)
