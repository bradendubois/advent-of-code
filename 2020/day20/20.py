from sys import stdin
from lark import Lark, LarkError
import math
import numpy as np
import itertools

l = stdin.read().split("\n\n")

puzzle = dict()

directions = ["left", "right", "up", "down"]

for piece in l:

    s = piece.split("\n")

    tile_id = int(s[0][5:-1])
    lines = s[1:]

    actual = [[x for x in s] for s in lines]
    cropped = [[x for x in s[1:-1]] for s in lines[1:-1]]

    puzzle[tile_id] = {
        "adjacent": 0,
        "sides": { d: None for d in directions },
        "reps": { d: set() for d in directions },
        "original": np.array(actual),
        "cropped": np.array(cropped)

    }

    up = lines[0]
    puzzle[tile_id]["reps"]["up"].update({up, up[::-1]})
    
    down = lines[-1]
    puzzle[tile_id]["reps"]["down"].update({down, down[::-1]})

    left = "".join(line[0] for line in lines)
    puzzle[tile_id]["reps"]["left"].update({left, left[::-1]})

    right = "".join(line[-1] for line in lines)
    puzzle[tile_id]["reps"]["right"].update({right, right[::-1]})


tile_ids = sorted(puzzle.keys())

for i, tile_a in enumerate(tile_ids):
    for j, tile_b in enumerate(tile_ids[i+1:], start=i+1):

        for a_direction, b_direction in itertools.product(directions, directions):                
                
            if puzzle[tile_a]["reps"][a_direction] & puzzle[tile_b]["reps"][b_direction] != set():
                puzzle[tile_a]["adjacent"] += 1
                puzzle[tile_b]["adjacent"] += 1

                puzzle[tile_a]["sides"][a_direction] = tile_b
                puzzle[tile_b]["sides"][b_direction] = tile_a

def left(tile_id):
    return puzzle[tile_id]["sides"]["left"]

def right(tile_id):
    return puzzle[tile_id]["sides"]["right"]

def up(tile_id):
    return puzzle[tile_id]["sides"]["up"]

def down(tile_id):
    return puzzle[tile_id]["sides"]["down"]


def rotate_tile(tile_id):
    puzzle[tile_id]["sides"]["up"], puzzle[tile_id]["sides"]["right"], puzzle[tile_id]["sides"]["down"], puzzle[tile_id]["sides"]["left"] = left(tile_id), up(tile_id), right(tile_id), down(tile_id)
    puzzle[tile_id]["cropped"] = np.rot90(puzzle[tile_id]["cropped"], 3)
    puzzle[tile_id]["original"] = np.rot90(puzzle[tile_id]["original"], 3)


def vertical_flip_tile(tile_id):
    puzzle[tile_id]["sides"]["down"], puzzle[tile_id]["sides"]["up"] = up(tile_id), down(tile_id)
    puzzle[tile_id]["cropped"] = np.flipud(puzzle[tile_id]["cropped"])
    puzzle[tile_id]["original"] = np.flipud(puzzle[tile_id]["original"])


def horizontal_flip_tile(tile_id):
    puzzle[tile_id]["sides"]["right"], puzzle[tile_id]["sides"]["left"] = left(tile_id), right(tile_id)
    puzzle[tile_id]["cropped"] = np.fliplr(puzzle[tile_id]["cropped"])
    puzzle[tile_id]["original"] = np.fliplr(puzzle[tile_id]["original"])



corners = [x for x in puzzle if puzzle[x]["adjacent"] == 2]

top_left = [c for c in corners if right(c) and down(c)][0]

current = top_left

starts = [current]

# Rotate tiles and construct first column
while puzzle[current]["sides"]["down"] is not None:

    next_tile = down(current)

    while left(next_tile):
        rotate_tile(next_tile)

    if down(next_tile) == current:
        vertical_flip_tile(next_tile)

    starts.append(next_tile)
    current = next_tile


tile_arrangement = []

# Construct each row from left-most tile in each column
for i, start in enumerate(starts):

    current = starts[i]
    r = [current]

    while len(r) < math.sqrt(len(puzzle)):

        current = r[-1]
        next_tile = right(current)

        if i == 0:      # First row

            if next_tile in corners and next_tile != top_left:    # Top Right Tile
                while up(next_tile) and right(next_tile):
                    rotate_tile(next_tile)
            
            else:
                while up(next_tile) is not None:
                    rotate_tile(next_tile) 

        else:       # Not first row - rotate to match tile in row above
            while up(next_tile) != tile_arrangement[i-1][len(r)]:
                rotate_tile(next_tile)

        if right(next_tile) == current:
            horizontal_flip_tile(next_tile)

        r.append(next_tile)

    tile_arrangement.append(r)


# Part One
print(corners, "=", np.prod(corners), "\n")

# Build the image
image = []
for tile_row in tile_arrangement:

    r = []

    for block in tile_row:
        
        cropped = puzzle[block]["cropped"]
        for i, x in enumerate(cropped):
            if len(r) - 1 < i:
                r.append([])

            r[i].extend(x)

    image.extend(r)


total = sum([row.count("#") for row in image])

image = np.array(image)

sea_monster = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   "
]

points = set()
for i, row in enumerate(sea_monster):
    for j, block in enumerate(row):
        if block == "#":
            points.add((i, j))

def scan_sea_monsters(img):
    
    c = np.copy(img)
    t = 0

    for y in range(len(img) - 2):
        for x in range(len(img[y]) - len(sea_monster[0]) - 1):
            if all((c[y + d_y][x + d_x] == "#") for d_y, d_x in points):
                for d_y, d_x in points:
                    c[y + d_y][x + d_x] = "O"
                t += 1

    return c, t


def display_image(arr):
    for r in arr:
        for c in r:
            print(c, end="")
        print()
    print()


all_orientations = []
tile_array = np.array(tile_arrangement)

for _ in range(8):

    if _ == 4:
        image = np.fliplr(image)
        tile_array = np.fliplr(tile_array)
    
    all_orientations.append((image, tile_array))
    image = np.rot90(image)
    tile_array = np.rot90(tile_array)


for tile_arrangement, tile_array in all_orientations:

    processed, sea_monsters = scan_sea_monsters(tile_arrangement)

    if sea_monsters != 0:

        # Print tile ids
        for r in tile_array:
            for id in r:
                print(id, " ", end="")
            print()
        print()

        display_image(processed)

        wasted = total - len(points) * sea_monsters
        message = "{} Sea Monsters; {} - ({} * {}) = {}".format(sea_monsters, total, sea_monsters, len(points), wasted)
        print(message)
