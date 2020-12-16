from sympy.ntheory.modular import crt
from sys import stdin

l = []

for line in stdin:
    l.append(line.strip())

wait = int(l[0])
busses = [int(x) if x.isdigit() else x for x in l[1].split(",")]

best_wait = 999999999999999
bus_id = 0

# Part One
for bus in busses:

    if bus == "x":
        continue

    temp = wait // bus * bus
    if temp < wait:
        temp += bus

    if temp < best_wait:
        best_wait = temp
        bus_id = bus

print(bus_id * (best_wait - wait))

# Part Two

m = []
v = []

for i, bus in enumerate(busses):

    if bus == "x":
        continue

    m.append(bus)
    v.append(bus - i)

print(crt(m, v)[0])
