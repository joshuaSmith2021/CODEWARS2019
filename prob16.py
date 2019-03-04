import sys
lines = sys.stdin.readlines()


for line in lines:
    line = line.strip()
    line =line.split()
    newlist = []
    for each in range(1, len(line)):
        if each == 1:
            if line[1] != line[0]:
                newlist.append(line[0])
                newlist.append(line[1])
            if line[1] == line[0]:
                newlist.append(line[0])
        if each > 1:
            if line[each].lower() == "is":
                if line[each - 2].lower() != line[each].lower():
                    newlist.append(line[each])
            elif line[each].lower() == "had":
                if line[each - 2].lower() != line[each].lower():
                    newlist.append(line[each])
            elif line[each].lower() != line[each - 1].lower():
                newlist.append(line[each])
    a = " ".join(newlist)
    print(a)
