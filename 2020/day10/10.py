from sys import stdin

l = []

for line in stdin:
    l.append(int(line.rstrip()))

full = [0] + sorted(l) + [max(l) + 3]

# Part One
diffs = [x - y for x, y in zip(full[1:], full[:-1])]

ones = diffs.count(1)
threes = diffs.count(3)

print(ones, threes, ones * threes)

# Part Two
c = [0] * (len(full) - 1) + [1]

for i in range(len(full) - 2, -1, -1):
    
    sum=0

    for j in range(i+1, len(full)):
        if full[j] - full[i] > 3:
            break
        sum+=c[j]

    c[i]=sum

print(c[0])
 