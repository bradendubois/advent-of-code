import itertools
from sys import stdin

numbers = []

for line in stdin:
    numbers.append(int(line.strip()))


def invalid(values, preamble):

    for i in range(preamble, len(values)):
        slc = values[i - preamble:i]
        target = values[i]

        sums = list(sum(x) for x in itertools.combinations(slc, 2))

        if target not in sums: 
            return target


# Part One
print(first_invalid := invalid(numbers, 25))

# Part 2
i = 2
while True:
    for j in range(len(numbers) - i):
        contiguous = numbers[j:j+i]
        if sum(contiguous) == first_invalid:
            print(min(contiguous) + max(contiguous))
            exit()
    i += 1
