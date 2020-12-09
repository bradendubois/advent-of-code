from collections import Counter
from sys import stdin

bags = dict()

for line in stdin:

    left, right = line.rstrip('\n.').split("contain")

    left = left.strip().removesuffix("bags").strip()
    right = [x.strip(" s").removesuffix(" bag") for x in right.split(", ")]

    vals = []

    for bag in right:
        s = bag.split(" ")
        if "no" == s[0]:
            break
        vals.append((" ".join(s[1:]).strip(" "), int(s[0])))
    bags[left] = vals

def all_parents(bag, searching):

    seen = set()
    parents = set()

    def _inner(cur):

        if cur in seen:
            return

        seen.add(cur)

        for b in searching:
            if any([cur == t[0] for t in searching[b]]):
                parents.add(b)
                _inner(b)
    
    _inner(bag)
    return parents

# Part 1
print(len(all_parents("shiny gold", bags)))

# Part 2
resolved = dict()

def resolve(bag, searching):

    total = 0

    for b in searching[bag]:
        left, right = b
        
        if left not in resolved:
            resolve(left, searching)

        total += right + right * resolved[left]
    
    resolved[bag] = total
    return total

print(resolve("shiny gold", bags))
