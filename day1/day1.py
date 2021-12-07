#!/usr/bin.env python3

with open("input.txt", 'r') as w:
    prev = int(w.readline())
    increase_count = 0
    for line in w:
        curr = int(line)
        if (curr - prev) > 0:
            increase_count += 1
        prev = curr
    print("Part 1 Increases: " + str(increase_count))

with open("input.txt", 'r') as w:
    summation = [int(w.readline()), int(w.readline()), int(w.readline())]
    prev = sum(summation)
    increase_count = 0
    for idx, line in enumerate(w):
        summation[idx%3] = int(line)
        curr = sum(summation)
        if (curr - prev) > 0:
            increase_count += 1
        prev = curr
    print("Part 2 Increases: " + str(increase_count))
