from sys import stdin
from math import sqrt

needed = int(input().strip())

def get_divisors(i):
    before_sqrt = [x for x in range(1, int(sqrt(i)) + 1) if i % x == 0]
    after = [i / d for d in before_sqrt if sqrt(i) != d]
    return before_sqrt + after

i = 0
while True:

    i += 1
    divisors = get_divisors(i)
    if sum(divisors) * 10 >= needed:
        print(i)
        exit(0)

