from itertools import chain, combinations
from sys import stdin

items = [int(x) for x in stdin]
powerset = chain.from_iterable(combinations(items, r) for r in range(len(items)+1))

sufficient = list(s for s in powerset if sum(s) == 150) 
lengths = [len(s) for s in sufficient]

print(len([s for s in lengths if s == min(lengths)]))
