from sys import stdin

instructions = list(map(lambda x: int(x), stdin.read().split("\n")))


def run(ins, p2=False):

    index, steps = 0, 0

    while 0 <= index < len(ins):

        steps += 1
        new_index = index + ins[index]
        
        if not p2 or ins[index] < 3:
            ins[index] += 1
        else:
            ins[index] -= 1

        index = new_index

    return steps


print(run(instructions.copy()))
print(run(instructions.copy(), True))
