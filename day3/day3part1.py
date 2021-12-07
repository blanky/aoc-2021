#!/usr/bin/end python3

bit_length = 12

with open("input.txt", 'r') as f:
    numbers = [int(x, 2) for x in f]

bit_totals = [0]*bit_length

for number in numbers:
    for i in range(bit_length):
        bit_totals[i] += 1 if ((1 << i) & number) else 0

gamma = 0
flipper = (2**bit_length) - 1
total_len = len(numbers)
print(bit_totals)
for idx, bit_total in enumerate(bit_totals):
    gamma += (1 << idx) if bit_total > (total_len/2) else 0

epsilon = gamma^flipper

power = epsilon*gamma

print("Gamma: %i" % (gamma))
print("Epsilon: %i" % (epsilon))
print("Power: %i" % (power))