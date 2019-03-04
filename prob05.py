import sys
lines = sys.stdin.readlines()

height = int(lines[0])
total = 0
for x in range(1, height + 1):
    total += x ** 2
print(total)
