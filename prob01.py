import sys
lines = sys.stdin.readlines()

for line in lines:
    print('While we seem to disagree on this issue, {}, I respect your opinion and look forward to further discussion!'.format(line.rstrip()))
