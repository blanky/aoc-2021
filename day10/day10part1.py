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
    return len(stack)

# part 1
score = 0
for line in lines:
    result = line_parser(line)
    if(type(result) is tuple):
        # print("%s - Expected %s got %s" % (line, result[0], result[1]))
        score += illegal[result[1]]
print("Part 1: %i"% (score))