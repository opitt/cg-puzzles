a1 = int(input())
n = int(input())
seen_at={a1:0}
seen_before=False

for pos in range(1,n):
    last=0 if not seen_before else pos-1-seen_before_at
    seen_before_at=seen_at.get(last,-1)
    seen_before=-1!=seen_before_at
    seen_at[last]=pos
    
print(last)
"""
Term 1: The first term is 0.
Term 2: Since we haven’t seen 0 before, the second term is 0.
Term 3: Since we had seen a 0 before, one step back, the third term is 1
Term 4: Since we haven’t seen a 1 before, the fourth term is 0
Term 5: Since we had seen a 0 before, two steps back, the fifth term is 2.
"""
