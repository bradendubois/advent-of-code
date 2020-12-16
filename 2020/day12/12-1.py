from sys import stdin

l = []

for line in stdin:
    l.append(line.rstrip())

angles = {
    0: "E",
    90: "S",
    180: "W",
    270: "N"
}

angle = 0

x = 0
y = 0

for instruction in l:

    direction = instruction[0]
    value = int(instruction[1:])

    if direction == "F":
        direction = angles[angle]
        
    elif direction == "R":
        angle += value
        angle %= 360

    elif direction == "L":
        angle -= value
        while angle < 0:
            angle += 360

    if direction == "N":
        y += value
        
    elif direction == "S":
        y -= value
    
    elif direction == "E":
        x += value
    
    elif direction == "W":
        x -= value

# Part One
print(abs(x) + abs(y))
