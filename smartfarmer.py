# given the first 3 years of harvest, the next year is the sum of the three prev years
# n>=3, y1, y2, y3
# expected 3 4 5 6 = 15
n, *r = map(int, input().split())
while n >= 3:
    r.append(sum(r[-3:]))
    n -= 1
print(r[-1] % (10 ** 9 + 7))

# n,a,b,c=map(int,input().split())
# d=0
# for i in range (n-2):d,a,b,c=a+b+c,b,c,d
# print(d%(10**9+7))
