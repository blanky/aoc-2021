#/usr/bin/env python3

# with open("test.txt", 'r') as f:
with open("input.txt", 'r') as f:
    segments = [x.replace('\n', '').split(' ') for x in f.readlines()]
    for idx in range(len(segments)):
        segments[idx].remove("|")

class SegmentSolver:
    def __init__(self, mystery):
        self.unsolved = mystery
    
    def solve_mystery(self):
        # wc2 =  1 = 'cf'
        wc2 = None
        # wc3 = 7 = 'acf'
        wc3 = None
        # wc4 = 4 = 'bcdf'
        wc4 = None
        # wc5 = 2 or 3 or 5 = 'adg'
        wc5 = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
        # wc6 = 0 or 6 or 9 = 'abfg'
        wc6 = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
        for mystery_segment in self.unsolved:
            char_set = set([char for char in mystery_segment])
            awc = len(char_set)
            if((awc == 2) and wc2 is None):
                wc2 = char_set
            elif((awc == 3) and wc3 is None):
                wc3 = char_set
            elif((awc == 4) and wc4 is None):
                wc4 = char_set
            elif(awc == 5):
                wc5 = wc5.intersection(char_set)
            elif(awc == 6):
                wc6 = wc6.intersection(char_set)
            else:
                pass
        if((wc2 == None) or (wc3 == None) or (wc4 == None) or (len(wc5) != 3) or (len(wc6) != 4)):
            print("Following unsolvable:")
            print(self.unsolved)
            print(wc2)
            print(wc3)
            print(wc4)
            print(wc5)
            print(wc6)
            raise NotImplementedError("Currently can't solve this.")
        sd = dict()
        # diff of wc2 and wc3 is 'a'
        sd['a'] = wc3.difference(wc2).pop()
        # intersection of wc5 and wc6 gives 'ag', knowing 'a' gives 'g'
        sd['g'] = wc5.intersection(wc6).difference(sd['a']).pop()
        # wc5 now gives solution for 'd'
        sd['d'] = wc5.difference({sd['a'], sd['g']}).pop()
        # diff of wc3 and wc4 gives 'abd', giving us 'b'
        sd['b'] = wc4.difference(wc3).difference({sd['a'], sd['d']}).pop()
        # intersection of wc4 and wc6 gives 'bf', giving us 'f'
        sd['f'] = wc4.intersection(wc6).difference(sd['b']).pop()
        # wc2 now gives us 'c'
        sd['c'] = wc2.difference(sd['f']).pop()
        # 'e' is diff between solved letters and all letters
        sd['e'] = set(['a', 'b', 'c', 'd', 'e', 'f', 'g']).difference(set([v for _,v in sd.items()])).pop()
        self.solver = dict()
        lookup = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
        for idx, combo in enumerate(lookup):
            new_combo = ''
            for i in combo:
                new_combo += sd[i]
            new_combo = ''.join(sorted(new_combo))
            self.solver[new_combo] = idx

    def getnum(self, seg):
        sort_seg = ''.join(sorted(seg))
        return self.solver[sort_seg]
    
    def get_output(self):
        return self.getnum(self.unsolved[-4])*1000 + \
               self.getnum(self.unsolved[-3])*100 + \
               self.getnum(self.unsolved[-2])*10 + \
               self.getnum(self.unsolved[-1])

total_output = 0
for puzzle in segments:
    solve_puzzle = SegmentSolver(puzzle)
    solve_puzzle.solve_mystery()
    output = solve_puzzle.get_output()
    total_output += output

print("Total output: {}".format(total_output))