from sys import stdin
import numpy as np


def result(table):

    t = []

    for i in range(len(table)):
        
        row = []
        for j in range(len(table[i])):

            around = [
                (i-1, j-1), (i-1, j), (i-1, j+1),
                (i, j-1), (i, j+1),
                (i+1, j-1), (i+1, j), (i+1, j+1) 
            ]

            ons = 0

            for point in around:
                y, x = point
                if 0 <= y < len(table) and 0 <= x < len(table[y]):
                    if table[y][x] == "#":
                        ons += 1
                    
            if table[i][j] == "#":
                row.append("#" if 2 <= ons <= 3 else ".")
            else:
                row.append("#" if ons == 3 else ".")

        t.append(row)

    return t

table = []
for line in stdin:
    table.append(line.strip())

for i in range(100):
    table = result(table)

on = 0
for row in table:
    for col in row:
        print(col, end="")
        if col == "#":
            on += 1
    print()

print("\n" + str(on))
