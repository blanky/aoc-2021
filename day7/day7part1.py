#!/usr/bin/env python3

# with open("test.txt", 'r') as f:
with open("input.txt", 'r') as f:
    crab_positions = list(map(int, f.readline().split(',')))

max_crab = max(crab_positions)
min_crab = min(crab_positions)

least_costly = 10000000
for i in range(min_crab, max_crab):
    fuel_cost = sum([abs(i-crab) for crab in crab_positions])
    if(fuel_cost < least_costly):
        least_costly = fuel_cost

print("Part 1: {}".format(least_costly))