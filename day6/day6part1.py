#!/usr/bin/env python3

DEBUG=False
def d_print(a):
    if DEBUG:
        print(a)

SIM_DAYS=80
# with open("test.txt", 'r') as f:
with open("input.txt", 'r') as f:
    laternfishes = list(map(int, f.readline().split(',')))

d_print("Initial state: {0}".format(laternfishes))
for i in range(SIM_DAYS):
    new_spawn = 0
    for j in range(len(laternfishes)):
        laternfishes[j] -= 1
        if(laternfishes[j] < 0):
            laternfishes[j] = 6
            new_spawn += 1
    d_print(new_spawn)
    laternfishes.extend([8]*new_spawn)
    d_print("After {0} day(s): {1}".format(i, laternfishes))

print("Simulated days: {}".format(SIM_DAYS))
print("Total lanternfish: {}".format(len(laternfishes)))