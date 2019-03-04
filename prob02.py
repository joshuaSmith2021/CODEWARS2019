import sys
lines = sys.stdin.readlines()


for line in lines:
    line = line.strip()
    line = line.split()
    hours = int(line[0])
    dist = int(line[1])
    speed = int(line[2])
    trav = hours * speed
    if trav >= dist:
        print(hours, dist, speed, '. I will make it!')
    else:
        print(hours, dist, speed, '. I will be late!')
    #print(line)
