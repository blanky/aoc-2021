#!/usr/bin.env python3

horizontal = 0
depth = 0
depth_part_2 = 0
aim = 0

with open("input.txt", 'r') as f:
    for line in f:
        [direction, steps] = line.split(" ")
        steps = int(steps)
        if direction == "forward":
            horizontal += steps
            depth_part_2 += (steps*aim)
        elif direction == "up":
            depth -= steps
            aim -= steps
        elif direction == "down":
            depth += steps
            aim += steps
        else:
            print("Error parsing: %s %i" % (direction, steps))

print("Part 1")
print("Horizontal: %i" % (horizontal))
print("Depth: %i" % (depth))
print("Multiply: %i\n" % (depth*horizontal))

print("Part 2")
print("Horizontal: %i" % (horizontal))
print("Depth: %i" % (depth_part_2))
print("Multiply: %i\n" % (depth_part_2*horizontal))

