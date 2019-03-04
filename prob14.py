import sys
lines = sys.stdin.readlines()
start = int(lines[0].strip())
current = int(lines[1].strip())
numbers = []
numbers.append(start)
numbers.append(current)
for x in range(0, 8):
    a = current + start
    numbers.append(current + start)
    start = current
    current = a
print(numbers)
