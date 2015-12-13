#!/usr/bin/env python

from collections import Counter

def read_input():
    with open('input_day3.txt') as src:
        return src.read()
        
moves = {
    '^': lambda p: (p[0], p[1] + 1),
    'v': lambda p: (p[0], p[1] - 1),
    '<': lambda p: (p[0] - 1, p[1]),
    '>': lambda p: (p[0] + 1, p[1])
}

def process(string):
    pos, poses = (0, 0), [(0, 0)]
    for char in string:
        pos = moves[char](pos)
        poses.append(pos)
    return Counter(poses)

tests = ['>', '^>v<', '^v^v^v^v^v']
for test in tests:
    print(process(test))

print('Part 1 answer:')
print(len(process(read_input())))

def process_with_robo(string):
    santa_string = string[::2]
    robo_string = string[1::2]
    counts = process(santa_string)
    counts.update(process(robo_string))
    return counts

tests[0] = '^v'
for test in tests:
    print(process_with_robo(test))

print('Part 2 answer:')
print(len(process_with_robo(read_input())))
