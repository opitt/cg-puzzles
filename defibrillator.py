def input():
    return next(input_data)

def sim_input():
    with (open("defibrillator-data.txt", "r")) as f:
        rows=f.readlines()
    for row in rows:
        yield row.rstrip()

input_data=sim_input()
#expected="Maison de la Prevention Sante"

import math

def g2rad(s):
    return math.radians(float(s.replace(",",".")))

def dist(lonA,latA,lonB,latB):
    x=(lonB-lonA)*math.cos((latA+latB)/2)
    y=latB-latA
    return math.hypot(x,y)*6371

lonA,latA = input(),input()
defi_dist=math.inf
for _ in range(int(input())):
    _,dadr,_,_,lonB,latB=input().split(";")
    d=dist(g2rad(lonA),g2rad(latA),g2rad(lonB),g2rad(latB))
    if d<defi_dist:
        defi_dist,defi_next=d,dadr

print(defi_next)
