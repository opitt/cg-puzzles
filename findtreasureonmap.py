def input():
    return next(input_data)


def sim_input():
    with (open("findtreasureonmap.txt", "r")) as f:
        rows = f.readlines()
    for row in rows:
        yield row.rstrip()


input_data = sim_input()


p = {}
for y in range(int(input())):
    l = input()
    for x, c in enumerate(l):
        if c in "abcdefghijklmnopqrstuvwxyz":
            p[c] = x,y
for c in sorted(p):
    print(*p[c])
