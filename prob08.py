import sys
lines = sys.stdin.readlines()

nums = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT',
        'NINE', 'TEN', 'ELEVEN', 'TWELVE']

for line in lines:
    line = line.rstrip()
    values = line.split()
    letters = []
    for val in values:
        if int(val) == 999:
            break
        num = list(nums[int(val)])
        for char in set(num):
            if letters.count(char) < num.count(char):
                needed = num.count(char) - letters.count(char)
                for i in range(needed):
                    letters.append(char)
    display = ''
    for letter in sorted(letters):
        display += letter + ' '
    print(line[:len(line) - 4] + '. ' + display)
