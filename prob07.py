import sys
lines = sys.stdin.readlines()

def isprime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def next_even(num):
    if num % 2 == 0:
        return num + 2
    else:
        return num + 1


def next_prime(num):
    while True:
        num += 1
        if isprime(num):
            return num


def next_square(num):
    while True:
        num += 1
        if int(num**0.5) == num**0.5:
            return num


def next_cube(num):
    while True:
        num += 1
        if round(int(num**(1/3)) / 100000) * 100000 + 1 == num**(1/3):
            return num

for line in lines:
    values = line.split()
    n = int(values[0])
    m = int(values[1])
    if m == 0:
        print(next_even(n))
    elif m == 1:
        print(next_prime(n))
    elif m == 2:
        print(next_square(n))
    elif m == 3:
        print(next_cube(n))
