#!/usr/bin/env python3

DEBUG=False
def d_print(a):
    if DEBUG:
        print(a)

SIM_DAYS=256
# with open("test.txt", 'r') as f:
with open("input.txt", 'r') as f:
    initial_state = list(map(int, f.readline().split(',')))

class SpawnGroup:
    def __init__(self, count):
        self.count = count
        self.spawn_day = 8
    
new_spawns = []
for i in range(SIM_DAYS):

    #Initial spawn parts
    day_spawn_count = 0
    for j in range(len(initial_state)):
        initial_state[j] -= 1
        if(initial_state[j] < 0):
            initial_state[j] = 6
            day_spawn_count += 1
    
    # Later spawns
    for new_spawn_group in new_spawns:
        new_spawn_group.spawn_day -= 1
        if(new_spawn_group.spawn_day < 0):
            new_spawn_group.spawn_day = 6
            day_spawn_count += new_spawn_group.count
    if(day_spawn_count > 0):
        new_spawns.append(SpawnGroup(day_spawn_count))
    
    # laternfishes.extend([8]*new_spawn)
    # print("After {0} day(s): {1}".format(i, len(laternfishes)))

total_lanternfish = len(initial_state) + sum([x.count for x in new_spawns])
print("Simulated days: {}".format(SIM_DAYS))
print("Total lanternfish: {}".format(total_lanternfish))