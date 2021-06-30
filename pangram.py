# pangram== if the sentence is made of all letter from the ascii alphabet. ignore other characters like space or #
# the fox jumps over the green grass dlgzy brown ikw cq

# import string
# w=input()
# r=" ".join([c for c in string.ascii_lowercase if c not in w])
# print((r,"Pangram")[len(r)<1])

import string
r = " ".join(sorted(set(string.ascii_lowercase) - set(input())))
print((r, "Pangram")[len(r) < 1])
