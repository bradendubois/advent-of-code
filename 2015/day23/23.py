from sys import stdin

instructions = [[i.strip(",") for i in x.split(" ")] for x in stdin.read().split("\n")]

def execute(instructions, registers):

    pointer = 0

    while 0 <= pointer < len(instructions):

        line = instructions[pointer]

        instruction = line[0]
        
        if instruction == "hlf":
            registers[line[1]] //= 2
            pointer += 1

        elif instruction == "tpl":
            registers[line[1]] *= 3
            pointer += 1

        elif instruction == "inc":
            registers[line[1]] += 1
            pointer += 1

        elif instruction == "jmp":
            pointer += int(line[1])

        elif instruction == "jie":
            if registers[line[1]] % 2 == 0:
                pointer += int(line[2])
            else:
                pointer += 1

        elif instruction == "jio":
            if registers[line[1]] == 1:
                pointer += int(line[2])
            else:
                pointer += 1

    return registers

# Part One
print(execute(instructions, {"a": 0, "b": 0})["b"])

# Part Two
print(execute(instructions, {"a": 1, "b": 0})["b"])
