import sys
lines = sys.stdin.readlines()


for line in lines:
    rope = line.strip()
    rope = int(rope)
    ropeSquared = rope * rope
    area = ropeSquared * 3.14159
    finArea = area * 0.75
    print(finArea)
