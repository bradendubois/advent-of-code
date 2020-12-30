from sys import stdin

lines = [x.split(" ") for x in stdin.read().split("\n")]

# Part One
print(len([l for l in lines if len(set(l)) == len(l)]))

# Part Two
lines = [["".join(sorted(word)) for word in x] for x in lines]
print(len([l for l in lines if len(set(l)) == len(l)]))
