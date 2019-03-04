import sys
import re
lines = sys.stdin.readlines()

pattern = re.compile(r'\d\w')

def numfind(x):
    dic = {"a" : 0, "b" : 0}
    counter = 0
    for each in x:
        each = each.replace('?', '')
        each = each.replace('!', '')
        each = each.replace('th', '')
        each = each.replace('rd', '')
        each = each.replace('nd', '')
        each = each.replace('st', '')
        if counter == 0:
            if each.isdecimal():
                dic["a"] = int(each)
                counter += 1
                continue
        if counter == 1:
            if each.isdecimal():
                dic["b"] = int(each)
    return(dic)

start_temp = int(lines[0].split()[1].strip())
name_owner = lines[1].split()[1].strip()
name_AI = lines[2].split()[1].strip()
del(lines[0:3])
for line in lines:
    line = line.strip()
    if "plus" in line or "added" in line:
        line = line.split()
        a = numfind(line)
        print("{} plus {} is {}, {}".format(a["a"], a["b"], a["a"] + a["b"], name_owner))
    elif "times" in line or "multiplied" in line:
        line = line.split()
        a = numfind(line)
        print("{} times {} is {}, {}".format(a["a"], a["b"], a["a"] * a["b"], name_owner))
    elif "to the" in line:
        line = line.split()
        a = numfind(line)
        print("{} to the power of {} is {}, {}".format(a["a"], a["b"], a["a"] ** a["b"], name_owner))
    elif "cold" in line or "Turn up" in line:
        print("Temperature has been raised, {}".format(name_owner))
        start_temp += 1
    elif "hot" in line or "AC" in line:
        print("Temperature has been lowered, {}".format(name_owner))
        start_temp -= 1
    elif "current temp" in line or "current temperature" in line:
        print("The currrent temperature is {}, {}".format(start_temp, name_owner))
    elif "call me" in line or "Call me" in line:
        line = line.split()
        name_owner = line[line.index("me") + 1]
        print("Okay, I'll call you {} from now on".format(name_owner))
    elif "your name" in line:
        print("My name is {}, {}".format(name_AI, name_owner))
    elif "call you" in line:
        line = line.split()
        name_AI = line[line.index("you") + 1]
        print("You can call me {} from now on".format(name_AI))
    elif "Tell me a joke" in line or "tell me a joke" in line:
        print("So this guy, a squirrel, and a dog walk into a bar")
    elif "better joke" in line:
        print("No")
    elif "pod" in line:
        print("I can't do that, {}".format(name_owner))
    else:
        print("I don't understand you, {}".format(name_owner))
