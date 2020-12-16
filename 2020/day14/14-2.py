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

        index = "{0:b}".format(int(index))
        while len(index) < len(mask):
            index = "0" + index

        for i, x in enumerate(mask):
            if x == "1":
                index = index[:i] + "1" + index[i + 1:]

            elif x == "X":
                index = index[:i] + "X" + index[i + 1:]

        allOptions = set()

        def gen_all(string, i):
            if i == len(string):
                allOptions.add(string)
                return
            elif string[i] == "X":
                for x in ["1", "0"]:
                    string = string[:i] + x + string[i + 1:]
                    gen_all(string, i + 1)
            else:
                gen_all(string, i + 1)

        gen_all(index, 0)
        for option in allOptions:
            memory[int(option, 2)] = value

t = 0
for k in memory:
    t += memory[k]

print(t)
