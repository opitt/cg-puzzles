# In the game of cribbage you have 5 cards with values between 1 and 10. Here you must output the number of groups of cards that can be added together to make 15.
# Input
# 5 lines containing the values of CARDs you hold.
# Output
# Line 1: The number of groups of cards that sum to 15.
# Constraints
# 1 <= CARD <= 10

# not my solution , but SHORT!!!
#c=[int(s)for s in open(0)]
#print(sum(15==sum(c[k]for k in range(5)if(1<<k)&i)for i in range(32)))

import itertools as t
b=[int(input()) for _ in "12345"]
print(sum([sum(x)==15 for i in range(6)for x in t.combinations(b,i)]))
