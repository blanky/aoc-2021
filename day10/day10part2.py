#!/usr/bin/env python3

# with open("test.txt", 'r') as f:
with open("input.txt", 'r') as f:
    lines = [i.replace('\n', '') for i in f]

opening_set = "([{<"
closing_set = ")]}>"

matching_pair = {
    "(":")",
    ")":"(",
    "[":"]",
    "]":"[",
    "{":"}",
    "}":"{",
    "<":">",
    ">":"<"
}

illegal = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

repair = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

def line_parser(line):
    stack = []
    for bracket in line:
        if(bracket in opening_set):
            stack.append(bracket)
        else:
            if(matching_pair[bracket] != stack[-1]):
                return (matching_pair[stack[-1]], bracket)
            else:
                stack.pop(-1)
    return stack

def repairer(stack):
    ret_val = ''
    for i in reversed(stack):
        ret_val += matching_pair[i]
    return ret_val

def repair_scorer(pointers):
    score = 0
    for bracket in pointers:
        score *= 5
        score += repair[bracket]
    return score

# part 2
score = 0
score_list = []
for line in lines:
    result = line_parser(line)
    if(type(result) is tuple):
        # print("%s - Expected %s got %s" % (line, result[0], result[1]))
        score += illegal[result[1]]
    else:
        if(len(result) > 0):
            completer = repairer(result)
            # print("%s - Complete by adding %s" % (line, completer))
            repair_score = repair_scorer(completer)
            # print("%s - %i total points" % (completer, repair_score))
            score_list.append(repair_score)

            

print("Part 1: %i"% (score))
score_list = sorted(score_list)
print("Part 2: %i" % (score_list[int(len(score_list)/2)]))