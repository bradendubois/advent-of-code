from sys import stdin
from itertools import product

lines = []
for line in stdin:
    if line:
        lines.append(line)
molecule = lines[-1].strip()

mapped = dict()
for line in lines[:-2]:
    s, t = [x.strip() for x in line.split("=>")]
    if s not in mapped:
        mapped[s] = []
    mapped[s].append(t)

results = set()
for word in mapped:
    
    count = molecule.count(word)
    copied = molecule.replace(word, "." + word + ".")

    for i in range(count):
        copied = copied.replace("." + word + ".", word + str(i), 1)

    for j in range(count):

        for alt in mapped[word]:
            result = copied.replace(word + str(j), alt)
            print("\n", result)
            result = "".join([c for c in result if c.isalpha()])
            print(result, "\n")
            results.add(result)

print(len(results))