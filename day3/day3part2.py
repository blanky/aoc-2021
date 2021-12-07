#!/usr/bin/end python3

with open("input.txt", 'r') as f:
# with open("test.txt", 'r') as f:
    pos = f.tell()
    bit_length = len(f.readline().splitlines()[0])
    f.seek(pos)
    numbers = [int(x, 2) for x in f]

def get_bit_totals(b_bit_length, b_numbers):
    b_bit_totals = [0]*b_bit_length
    for number in b_numbers:
        for i in range(b_bit_length):
            b_bit_totals[i] += 1 if ((1 << i) & number) else 0
    return b_bit_totals

bit_totals = get_bit_totals(bit_length, numbers)
gamma = 0
flipper = (2**bit_length) - 1
total_len = len(numbers)
for idx, bit_total in enumerate(bit_totals):
    gamma += (1 << idx) if bit_total > (total_len/2) else 0
epsilon = gamma^flipper
power = epsilon*gamma

print("Gamma: %i" % (gamma))
print("Epsilon: %i" % (epsilon))
print("Power: %i" % (power))

# find out if matcher is 0 or 1 in that bit
# bit mask and xnor the matcher and number&bitmask
# if result is 0, it matches, else delete
def get_matching_list(bit_mask, matcher, players):
    survivors = list()
    for player in players:
        if ((player&bit_mask)^matcher) == 0:
            survivors.append(player)
    return survivors

def recursive_find_match(config, b_bit_totals, b_numbers):
    bit_lookup = len(b_bit_totals)-1
    bit_mask = 1 << bit_lookup
    if config == "more":
        matcher = (1 << bit_lookup) if b_bit_totals[bit_lookup] >= len(b_numbers)/2 else 0
    else:
        matcher = (1 << bit_lookup) if b_bit_totals[bit_lookup] < len(b_numbers)/2 else 0
    survivors = get_matching_list(bit_mask, matcher, b_numbers)
    if len(survivors) == 1:
        return survivors[0]
    survivor_bit_totals = get_bit_totals(bit_lookup, survivors)
    return recursive_find_match(config, survivor_bit_totals, survivors)

o2 = recursive_find_match("more", bit_totals, numbers)
co2 = recursive_find_match("less", bit_totals, numbers)
print("O2 generator: %i" % (o2))
print("CO2 scrubber: %i" % (co2))
print("Life support rating: %i" % (o2 * co2))