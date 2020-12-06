from sys import stdin

l = []

for line in stdin:

    l.append(line.rstrip())

seats = set()

for boarding_pass in l:

    r = int(boarding_pass[:-3].replace("F", '0').replace("B", '1'), 2)
    c = int(boarding_pass[-3:].replace("L", '0').replace("R", '1'), 2)

    seats.add(r * 8 + c)

low = min(seats)
high = max(seats)

# Part 1
print(high)

# Part 2
print(seats ^ set(range(low, high + 1)))
