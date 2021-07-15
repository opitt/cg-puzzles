def input():
    return next(input_data)


def sim_input():
    with (open("achildsplay.txt", "r")) as f:
        rows = f.readlines()
    for row in rows:
        yield row.rstrip()


input_data = sim_input()

w, h = [int(i) for i in input().split()]
n = int(input())
lines = []
x, y = 0, 0
d = "N"
dif = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
right = {"N": "E", "E": "S", "S": "W", "W": "N"}

for i in range(h):
    lines.append([*input()])
    try:
        x = lines[-1].index("O")
        y = i
    except:
        pass

path = []

for moves in range(n+1):   
    while lines[y + dif[d][0]][x + dif[d][1]] == "#":
        d = right[d]
    else:
        wp = (y, x, d)
    if wp in path:
        break
    path.append(wp)
    y += dif[d][0]
    x += dif[d][1]

loop_start=path.index(wp)
loop_len = len(path[loop_start:])
move_ends=loop_start+(n-moves)%loop_len
wp=path[move_ends]

print(wp[1],wp[0]) # x y
