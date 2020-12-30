from sys import stdin

square = int(stdin.read())

i = 1

while (i ** 2) < square:
    i += 2

start = i**2
corner = (start - (i - 2) ** 2) // 4

n = (i - 1) - min(square % corner, corner - (square % corner))

# Part One
print(n)

# Part Two
# Thank you, OEIS
with open("A141481.txt") as f:
    values = [line.split(" ") for line in f.read().split("\n")]

print(min(filter(lambda x: x > square, map(lambda x: int(x[1]), values))))
