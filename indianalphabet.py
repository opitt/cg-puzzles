from string import ascii_lowercase as a

n = int(input())  # number of letters
line = a[:n][::-1]
out = []
for i in range(1, n + 1):
    s = "-".join(line[:i]).rjust(n * 2 - 1, "-")
    out.append(s[:-1] + s[::-1])
print("\n".join(out))
print("\n".join(out[1::-1]))
