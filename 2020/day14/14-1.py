from sys import stdin

l = []

for line in stdin:
    l.append(line.rstrip())

mask = None
memory = dict()

for line in l:

    left, right = line.split(" = ")

    # Set Mask
    if "mask" in line:
        mask = right
        
    # Write memory
    else:
        address = left.split("[")[1].strip("]")

        index = int(address)
        value = int(right)

        value_bin = "{0:b}".format(value)
        while len(value_bin) < len(mask):
            value_bin = "0" + value_bin

        for i, x in enumerate(mask):
            if x != "X":
                value_bin = value_bin[:i] + x + value_bin[i + 1:]

        memory[index] = int(value_bin, 2)

t = 0
for k in memory:
    t += memory[k]

print(t)
