#!/usr/bin/env python

def area(l, w, h):
    sides = (l*w, w*h, h*l)
    smallest = min(sides)
    area = sum(2*s for s in sides) + smallest
    return area

def s2tup(string):
    return tuple(int(s) for s in string.split('x'))

dim1 = '2x3x4'
print('dim1: ', area(*s2tup(dim1)))

dim2 = '1x1x10'
print('dim2: ', area(*s2tup(dim2)))

def read_input():
    with open('input_day2.txt') as src:
        return [s2tup(l) for l in src.readlines()]

input = read_input()
areas = [area(*i) for i in read_input()]
print(sum(areas))

def ribbon(l, w, h):
    perimeters = (2 * (l + w), 
                  2 * (w + h), 
                  2 * (h + l))
    smallest = min(perimeters)
    volume = l * w * h
    return smallest + volume

print('dim1: ', ribbon(*s2tup(dim1)))
print('dim2: ', ribbon(*s2tup(dim2)))
ribbons = [ribbon(*i) for i in read_input()]
print(sum(ribbons))
