from sys import stdin

l = []

for line in stdin:

    l.append(line.rstrip())


def bsp(low, high, low_c, s):

    l = low
    h = high

    for c in s:

        mid = (h + l) // 2

        if c == low_c:
            h = mid

        else:
            l = mid + 1
    
    return h


seats = set()

for boarding_pass in l:
    r, c = bsp(0, 127, "F", boarding_pass[:-3]), bsp(0, 7, "L", boarding_pass[-3:])
    seats.add(r * 8 + c)

low = min(seats)
high = max(seats)

# Part 1
print(high)

# Part 2
print(seats ^ set(range(low, high + 1)))
