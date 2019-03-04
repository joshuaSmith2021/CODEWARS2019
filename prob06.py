import sys
lines = sys.stdin.readlines()


start = int(lines[0].strip())
total = 0
for each in range(1, start):
    total += 4 * (start - each)
print(total)
