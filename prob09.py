import sys
lines = sys.stdin.readlines()

combos = {
    'scissors paper': {'display': 'Scissors cuts Paper', 'winner': 'scissors'},
    'paper rock': {'display': 'Paper covers Rock', 'winner': 'paper'},
    'rock lizard': {'display': 'Rock crushes Lizard', 'winner': 'rock'},
    'lizard spock': {'display': 'Lizard poisons Spock', 'winner': 'lizard'},
    'spock scissors': {'display': 'Spock smashes Scissors', 'winner': 'spock'},
    'scissors lizard': {'display': 'Scissors decapitates Lizard', 'winner': 'scissors'},
    'lizard paper': {'display': 'Lizard eats Paper', 'winner': 'lizard'},
    'paper spock': {'display': 'Paper disproves Spock', 'winner': 'paper'},
    'spock rock': {'display': 'Spock vaporizes Rock', 'winner': 'spock'},
    'rock scissors': {'display': 'Rock crushes Scissors', 'winner': 'rock'}
}

for line in lines:
    line = line.rstrip()
    originals = line.split()
    values = line.split()
    keey = values[0].lower() + ' ' + values[1].lower()
    if keey in combos.keys():
        given = originals[0].lower()
        winner = combos[keey]['winner']
        if given == winner:
            print(winner.upper() + ' WINS,', end=' ')
        else:
            print(given.upper() + ' LOSES,', end=' ')
        print(combos[keey]['display'])
        continue
    values = list(reversed(values))
    keey = values[0].lower() + ' ' + values[1].lower()
    if keey in combos.keys():
        given = originals[0].lower()
        winner = combos[keey]['winner']
        if given == winner:
            print(winner.upper() + ' WINS,', end=' ')
        else:
            print(given.upper() + ' LOSES,', end=' ')
        print(combos[keey]['display'])
        continue
    print('TIE, {0} does not affect {1}'.format(originals[0].upper(), originals[1].upper()))
