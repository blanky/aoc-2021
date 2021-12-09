#!/usr/bin/env python3

# with open("test.txt", 'r') as f:
with open("input.txt", 'r') as f:
    height_map = []
    for line in f:
        line = line.replace('\n', '')
        height_map.append([int(x) for x in line])

def is_lowpoint(x, y, hmap):
    left = False
    if(x == 0):
        left = True
    elif(hmap[y][x] < hmap[y][x-1]):
        left = True
    right = False
    if(x == len(hmap[0])-1):
        right = True
    elif(hmap[y][x] < hmap[y][x+1]):
        right = True
    up = False
    if(y == 0):
        up = True
    elif(hmap[y][x] < hmap[y-1][x]):
        up = True
    down = False
    if(y == len(hmap)-1):
        down = True
    elif(hmap[y][x] < hmap[y+1][x]):
        down = True
    return left and right and up and down

def basin_size(x, y, hmap):
    X = 0
    Y = 1
    #algo: check all points in set.
    # each point, check the 4 surrounding
    # if not past edge and not 9, add to set
    # after each iteration, check if set size has changed, if not, return that size
    basin_set = {(x,y)}
    basin_size = len(basin_set)
    while True:
        for point in list(basin_set):
            # left
            if(point[X] != 0 and hmap[point[Y]][point[X]-1] != 9):
                basin_set.add((point[X]-1, point[Y]))
            # right
            if(point[X] != len(hmap[0])-1 and hmap[point[Y]][point[X]+1] != 9):
                basin_set.add((point[X]+1, point[Y]))
            # up
            if(point[Y] != 0 and hmap[point[Y]-1][point[X]] != 9):
                basin_set.add((point[X], point[Y]-1))
            #down
            if(point[Y] != len(hmap)-1 and hmap[point[Y]+1][point[X]] != 9):
                basin_set.add((point[X], point[Y]+1))
        if(len(basin_set) == basin_size):
            return len(basin_set)
        else:
            basin_size = len(basin_set)



basin_sizes = []

for y in range(len(height_map)):
    for x in range(len(height_map[0])):
        if(is_lowpoint(x,y,height_map)):
            basin_sizes.append(basin_size(x,y,height_map))

basin_sizes = sorted(basin_sizes)
part2 = basin_sizes[-1]*basin_sizes[-2]*basin_sizes[-3]
print("Part 2: {}".format(part2))