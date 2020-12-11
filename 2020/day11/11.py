from sys import stdin

l = []

for line in stdin:
    l.append([c for c in line.rstrip()])


def same(s, t):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] != t[i][j]:
                return False
    return True


# Part 1
def adjacent(s, i, j, i_x, j_x):
    if 0 <= i + i_x < len(s) and 0 <= j + j_x < len(s[i]):
        return s[i + i_x][j + j_x] == "#"
    return False


# Part 2
def directional(s, i, j, i_x, j_x):

    t_i = i + i_x
    t_j = j + j_x

    while 0 <= t_i < len(s) and 0 <= t_j < len(s[t_i]):
        if s[t_i][t_j] == "L":
            return False
        elif s[t_i][t_j] == "#":
            return True
        
        t_i += i_x
        t_j += j_x

    return False
    

def iteration(s, f, rule_v):

    def occupied_check(y, x):
        t = 0

        for t_y in [-1, 0, 1]:
            for t_x in [-1, 0, 1]:
                if t_y == 0 and t_x == 0:
                    continue
                t += f(s, y, x, t_y, t_x)

        return t

    c = [[x for x in nl] for nl in s]

    for i in range(len(c)):
        for j in range(len(c[i])):

            around = occupied_check(i, j)

            if s[i][j] == "L" and around == 0:
                c[i][j] = "#"

            elif s[i][j] == "#" and around >= rule_v:
                c[i][j] = "L"  

    return c


def stabilize(initial, search, rule_v):

    previous = initial
    current = iteration(initial, search, rule_v)

    while not same(previous, current):
        previous = current
        current = iteration(current, search, rule_v)
    
    return sum([x.count("#") for x in current])


print(stabilize(l, adjacent, 4))
print(stabilize(l, directional, 5))
