#!/usr/bin/env python3

translate = {'(': 1, ')': -1}

with open("input_day1.txt") as fhandle:
    data = [translate[char] for char in fhandle.read()]
    
    position, index = 0, 0
    for val in data:
        index += 1
        position += val
        if position == -1:
            print(index)
            break 
