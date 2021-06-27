expected="""-119
-78
-200
-156
285
-281
244
1481
-281
-81
1316
566
122
-281
-730
1072
-78
-447
1163
129
548
-281
10
-1556
-41
0
-200
3
-1225
200
-1559
-119
0
122
88
-285
-153
1884
1197
-1214
-444
1245
-807
-244
-285
-481
41
-200
1762
338
1478
247
1441
0
-41
1638
-119
166
403
122
488
1150
488
122
491
203
-119
-119
-434
-3
1140
1353
0
485
366
-1756
829
-1475
-34
-444
-766
-1656
-281
-3
-566
654
1072
-849
-278
-3
-766
447
10
125
688
691
366
-81
0
-1021""".splitlines()

import sys
from operator import add, sub, mul

OP={"ADD": add, "MULT": mul, "SUB": sub, "VALUE": add }

def input():
    return next(input_data)

def sim_input():
    with (open("test11.txt", "r")) as f:
        rows=f.readlines()
    for row in rows:
        yield row.rstrip()

input_data=sim_input()

def p(*args):
    print(">>>", *args, file=sys.stderr, flush=True)

cells=[]
for _ in range(int(input())):
    row=input()
    row=row.replace("_", "0") #treat VALUE as number+0
    if "$" in row:
        content=row
    else:
        op,arg1,arg2=row.split()
        content=f"{OP[op](int(arg1),int(arg2))}"
    cells.append(content)

#as long as there are unresolved references, go through the sheet, and try to replace them with correct value
while len(list(filter(lambda c: "$" in c,cells))):
    #parse for unresolved references
    for i in [ i for i,cell in enumerate(cells) if "$" in cell]:
        op,arg1,arg2=cells[i].split()
        if "$" in arg1:
            ref=int(arg1[1:])
            refval=cells[ref]
            arg1 = refval if "$" not in refval else arg1
        if "$" in arg2:
            ref=int(arg2[1:])
            refval=cells[ref]
            arg2 = refval if "$" not in refval else arg2
        cells[i]=f"{op} {arg1} {arg2}"
        if "$" not in cells[i]:
            op,arg1,arg2=cells[i].split()
            cells[i]=f"{OP[op](int(arg1),int(arg2))}"

for c,e in zip(cells,expected):
    print(c==e, c,e)
