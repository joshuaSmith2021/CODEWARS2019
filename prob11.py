import sys
lines = sys.stdin.readlines()

width = int(lines[0].split()[0])
del(lines[0])

rows = []
for line in lines:
    line = line.rstrip()
    rows.append(line)
for row in reversed(sorted(rows)):
    print(row)

for i in range(width + 1):
    print(str(i)[-1], end='')
print()
