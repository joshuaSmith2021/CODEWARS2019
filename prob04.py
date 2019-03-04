import sys
lines = sys.stdin.readlines()

sets = int(lines[0])
del(lines[0])

def decimals(num):
    vals = num.split('.')
    if len(vals) == 1:
        return vals[0] + '.00'
    elif len(vals[1]) == 1:
        vals[1] += '0'
        return vals[0] + '.' + vals[1]
    else:
        return num


def calc(rate, spent):
    pass

for i in range(sets):
    calc(lines[i], lines[i + 1])


print(decimals('500.978'))
