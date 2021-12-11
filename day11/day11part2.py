#!/usr/bin/env python3

# with open("test.txt", 'r') as f:
with open("input.txt", 'r') as f:
    map = []
    for line in f:
        line = line.replace('\n', '')
        map.append([int(i) for i in line])


def flash(x, y, map):
    surrounding_points = []
    for dx in range(-1, 2, 1):
        for dy in range(-1, 2, 1):
            surrounding_points.append((x+dx, y+dy))
    surrounding_points.remove((x,y))
    max_x = len(map[0])
    max_y = len(map)
    for point in surrounding_points:
        if (not (point[0] < 0 or point[1] < 0 or point[0] >= max_x or point[1] >= max_y)) and \
           (map[point[1]][point[0]] != 0):
            map[point[1]][point[0]] += 1
    return map
        
def new_flashes(map):
    for y in range(len(map)):
        for x in range(len(map)):
            if(map[y][x] > 9):
                return True

def background_gain(map):
    for y in range(len(map)):
        for x in range(len(map)):
            map[y][x] += 1
    return map

def print_map(map):
    for line in map:
        line_str = ''
        for i in line:
            line_str += str(i)
        print(line_str)


print("Before steps")
print_map(map)
flashes = 0
step = 0
while flashes != len(map[0])*len(map):
    flashes = 0
    map = background_gain(map)
    while new_flashes(map):
        for y in range(len(map)):
            for x in range(len(map[0])):
                if(map[y][x] > 9):
                    flashes += 1
                    map = flash(x, y, map)
                    map[y][x] = 0
    step += 1
    print("Step %i" % (step))
    print_map(map)
