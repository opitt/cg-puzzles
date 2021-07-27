"""
Encode the message!
Expect a list of numbers separated by space:
60 610 641
Each number represents a letter.
Each digit represents the bit set (counting from right).
60 = 1000000 = A
610= 1000010 = C
641= 1001001 = R
print the result
ACR
"""
for m in input().split():print(end=chr(sum(1<<int(c)for c in m)))
