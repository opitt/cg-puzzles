def input():
    return next(input_data)


def sim_input():
    with (open("enoughingredientsfororders.txt", "r")) as f:
        rows = f.readlines()
    for row in rows:
        yield row.rstrip()


input_data = sim_input()

i = input
_ = i()  # number of ingredients
I = i().split() #ingredients
O=[]
for _ in range(int(i())): # number of orders
    O.extend(i().split()) # order
for o in O:
    n=o in I
    if n:
        del I[I.index(o)]
    else:
        break
print(("NO", "YES")[n])
