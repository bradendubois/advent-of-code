from sys import stdin

puzzle_input = "215694783"

c = [int(x) for x in puzzle_input]

def solve(cup_list, moves):

    cups = { cup: cup_list[(i+1) % len(cup_list)] for i, cup in enumerate(cup_list)}

    moves_made = 0

    current_cup = int(puzzle_input[0])

    while moves_made < moves:

        p1 = cups[current_cup]
        p2 = cups[p1]
        p3 = cups[p2]

        cups[current_cup] = cups[p3]

        target = current_cup - 1
        if target < 1:
            target = max(cups)
        
        while target in [p1, p2, p3] or target == 0:
            target -= 1
            if target < 1:
                target = max(cups)
        
        cups[p3] = cups[target]
        cups[target] = p1

        current_cup = cups[current_cup]

        moves_made += 1

    return cups


# Part One
r1 = solve(c, 100)
cur = 1
t = []
while r1[cur] != 1:
    t.append(cur := r1[cur])
print("".join(str(x) for x in t))

# Part Two
c.extend(range(max(c) + 1, 1000001))
r2 = solve(c, 10000000)
print(r2[1] * r2[r2[1]])
