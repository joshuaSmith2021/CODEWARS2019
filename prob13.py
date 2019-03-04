import sys
lines = sys.stdin.readlines()


n1 = lines[0].strip()
n2 = lines[2].strip()
d1 = lines[1].strip()
d2 = lines[3].strip()

if n1 == "X":
    print(float(n2)/float(d2) * float(d1))
if n2 == "X":
    print(float(n1)/float(d1) * float(d2))
if d1 == "X":
    print((float(n1) * float(d2)) / float(n2))
if d2 == "X":
    print((float(n2) * float(d1)) / float(n1))
