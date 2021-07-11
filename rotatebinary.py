#given a integer, convert it to binary and rotate the first n bits for all the bits
# print the integer ater each rotation

b=f"{int(input()):0b}"
for i in range(len(b)):print(int(b:=b[i]+b[:i]+b[i+1:],2),b)
