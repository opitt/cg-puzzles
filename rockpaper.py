def input():
    return next(input_data)

def sim_input():
    with (open("rockpaper.txt", "r")) as f:
        rows=f.readlines()
    for row in rows:
        yield row.rstrip()

input_data=sim_input()

from collections import defaultdict
from copy import deepcopy
from os import sep

beats={"CP":"C","PC":"C",
    "PR":"P","RP":"P",
    "RL":"R","LR":"R",
    "LS":"L","SL":"L",
    "SC":"S","CS":"S",
    "CL":"C","LC":"C",
    "LP":"L","PL":"L",
    "PS":"P","SP":"P",
    "SR":"S","RS":"S",
    "RC":"R","CR":"R",
}

def battle(a,b):
    #[player,sign]
    # returns winner, looser
    if a[1]==b[1]:
        return (a,b) if int(a[0])<int(b[0]) else (b,a)
    elif beats[a[1]+b[1]]==a[1]:
        return a,b
    else:
        return b,a

winner=defaultdict(list)
n = int(input())
players=[input().split() for i in range(n)]
print (players)
while len(players)>1:
    nextround=[]
    for i in range(0,len(players)-1,2):
        win,los=battle(players[i],players[i+1])
        winner[win[0]].append(los[0])
        nextround.append(win)
    players = deepcopy(nextround)
print(players[0][0], " ".join(winner[players[0][0]]), sep="\n")
