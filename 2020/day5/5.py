from sys import stdin

l = []

for line in stdin:

    l.append(line.rstrip())


def bsp(low, high, low_c, s):

    mid = (high + low) // 2

    if low == high:
        return low

    else:
        r = (low, mid) if s[0] == low_c else (mid + 1, high)
        return bsp(*r, low_c, s[1:])

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
