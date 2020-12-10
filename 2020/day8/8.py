from collections import Counter
from sys import stdin

code = []

for line in stdin:

    l = line.strip().split(" ")

    code.append((l[0], int(l[1])))


def execute(instructions):

    acc = 0
    i = 0
    seen = set()

    while True:

        if i in seen:
            return False, acc
        
        elif i == len(instructions):
            return True, acc
        
        seen.add(i)

        instruction, value = instructions[i]

        if instruction == "nop":
            i += 1
        
        elif instruction == "jmp":
            i += value
        
        else:
            i += 1
            acc += value

# Part One
print(execute(code)[1])

# Part Two
for i in range(len(code)):
    
    save = code[i]

    replace = None

    if save[0] == "jmp":
        replace = ("nop", save[1])
    elif save[0] == "nop":
        replace = ("jmp", save[1])

    if replace:
        code[i] = replace
        if (res := execute(code))[0]:
            print(res[1])
            exit()
        code[i] = save
