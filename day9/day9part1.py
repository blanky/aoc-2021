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

low_points = []

for y in range(len(height_map)):
    for x in range(len(height_map[0])):
        if(is_lowpoint(x,y,height_map)):
            low_points.append(height_map[y][x])

print("Part 1: {}".format(sum(low_points)+len(low_points)))