from collections import Counter
from sys import stdin

l = []

for line in stdin:

    l.append(line.rstrip())


groups = []

cur = dict()
count = 0

for line in l:

    if line == "" and len(cur) > 0:
        groups.append((cur, count))

        cur = dict()
        count = 0
    
    else:
        count += 1
        for char in line:
            if char not in cur:
                cur[char] = 0
            cur[char] += 1


# Part 1
print(sum([len(group[0]) for group in groups]))

# Part 2
everyone = 0
for group in groups:
    answers, size = group
    all_yes = len([x for x in answers if answers[x] == size])
    everyone += all_yes
print(everyone)
