def input():
    return next(input_data)


def sim_input():
    with (open("prefix_code.txt", "r")) as f:
        rows = f.readlines()
    for row in rows:
        yield row.rstrip()


input_data = sim_input()
# above his line is input simulation code
"""
Given a fixed set of characters, a code is a table that gives the encoding to use for each character.

A prefix code is a code with the prefix property, which is that there is no character with an encoding that is a prefix (initial segment) of the encoding of another character.

Your goal is to decode an encoded string using the given prefix code, or say that is not possible.

Example of encoding.
Given the string "abracadabra" and the prefix code:
a -> 1
b -> 001
c -> 011
d -> 010
r -> 000
The resulting encoding is: 10010001011101010010001

Thus, if your are given the code above and the input 10010001011101010010001, you should output the string "abracadabra".

With the same prefix code, if the input is 0000, then you should tell that there is an error at index 3. Indeed, the first three characters of this input can be decoded to give an 'r', but that leaves 0, which cannot be decoded.

Input
Line 1: A single integer N representing the number of association in the prefix-code table.
Next N lines: A binary code Bi and an integer Ci, which tells that the character with ASCII code Ci will be encoded by Bi.
Next line: The binary code S of an encoded string.
Output
- If it is not possible to decode the encoded string, print DECODE FAIL AT INDEX i with i the first index in the encoded string where the decoding fails (index starts from 0).
- Otherwise print the decoded string.
"""
n = int(input())
code = {b:chr(int(c)) for b, c in [input().split() for _ in range(n)]}
#code = {b:chr(int(c)) for _ in range(n) for b, c in [input().split()]} 
s = input()

res = ""
idx = 0
found = len(code)>0
while found and len(s):
    for b in code.keys():
        found = s.startswith(b)
        if found:
            res += code[b]
            s = s[len(b):]
            idx += len(b)
            break

if not found:
    print(f"DECODE FAIL AT INDEX {idx}")
else:
    print(res)
