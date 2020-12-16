from sys import stdin

l = []

for line in stdin:
    l.append(line.rstrip())

x = 0
y = 0

waypoint_x = 10
waypoint_y = 1

def rotate(v):
    global waypoint_x, waypoint_y
    rotations = abs(v // 90)
    l, r = (-1, 1) if v < 0 else (1, -1)

    for _ in range(rotations):
        waypoint_x, waypoint_y = l * waypoint_y, r * waypoint_x


for instruction in l:

    direction = instruction[0]
    value = int(instruction[1:])

    if direction == "F":
        x += waypoint_x * value
        y += waypoint_y * value

    elif direction == "R":
        rotate(value)
    
    elif direction == "L":
        rotate(-value)

    elif direction == "N":
        waypoint_y += value

    elif direction == "S":
        waypoint_y -= value

    elif direction == "E":
        waypoint_x += value

    elif direction == "W":
        waypoint_x -= value


# Part Two
print(abs(x) + abs(y))

