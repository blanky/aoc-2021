#!/usr/bin/env python3

# with open("test.txt", 'r') as f:
with open("input.txt", 'r') as f:
    crab_positions = list(map(int, f.readline().split(',')))

max_crab = max(crab_positions)
min_crab = min(crab_positions)

least_costly = 10000000000000
for i in range(min_crab, max_crab):
    # triangular number cost function
    fuel_cost = sum([(abs(i-crab)*(abs(i-crab)+1))/2 for crab in crab_positions])
    if(fuel_cost < least_costly):
        least_costly = fuel_cost

print("Part 2: {}".format(least_costly))