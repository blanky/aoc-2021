#!/usr/bin/env python3

class Map:
    def __init__(self, size_x, size_y):
        self.map = [[0]*size_x for i in range(size_y)]
        
    
    def __str__(self):
        map_str = ""
        for y in self.map:
            for x in y:
                map_str += "%i " % (x)
            map_str += "\n"
        return map_str
    
    def add_line(self, x0, y0, x1, y1):
        if(x0 == x1):
            if(y0 > y1):
                iterator = range(y0, y1-1, -1)
            else:
                iterator = range(y0, y1+1, 1)
            for y in iterator:
                self.add_point(x0, y)
        else:
            if(x0 > x1):
                iterator = range(x0, x1-1, -1)
            else:
                iterator = range(x0, x1+1, 1)
            for x in iterator:
                self.add_point(x, y0)

    def add_point(self, x, y):
        self.map[y][x] += 1

    def count_above_two(self):
        count = 0
        for y in self.map:
            for x in y:
                count += 1 if x >= 2 else 0
        return count


# MAX_X = MAX_Y = 10
# with open("test.txt", 'r') as f:
MAX_X = MAX_Y = 1000
with open("input.txt", 'r') as f:
    textlines = f.readlines()
    vent_map = Map(MAX_X, MAX_Y)
    for i in textlines:
        j = i.replace(' -> ', ',').replace('\n', '').split(',')
        [x0,y0,x1,y1] = map(int, j)
        if(x0 == x1 or y0 == y1):
            vent_map.add_line(x0, y0, x1, y1)
        else:
            print("Not a straight line: %s" % (i), end='')
# print(vent_map)
print("Points over two: %i" % (vent_map.count_above_two()))

