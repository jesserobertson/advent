#!/usr/bin/env python

from collections import Counter
from itertools import tee

def has_three_vowels(string):
    count = 0
    for char in string:
        if char in set('aeiou'):
            count += 1
        if count == 3:
            return True
    return False

test_3v = ['aeiou', 'aei', 'xazegov', 'aeiouaeiouaeiou']
for test in test_3v:
    assert has_three_vowels(test) is True
print('has_three_vowels passes tests')

def has_double_letters(string):
    a, b = tee(string)
    next(b, None)
    for pair in zip(a, b):
        if pair[0] == pair[1]:
            return True
    return False

test_dl = ['xx', 'abcdde', 'aabbccdd']
for test in test_dl:
    assert has_double_letters(test) is True
print('has_double_letters passes tests')

def doesnt_have_strings(string):
    not_allowed = ['ab', 'cd', 'pq', 'xy']
    for na in not_allowed:
        if na in string:
            return False
    return True

test_na = ['ab', 'acda', 'aprrpapq', 'xyxxyx']
for test in test_na:
    assert doesnt_have_strings(test) is False
print('doesnt_have_strings passes tests')

def is_nice(string):
    tests = [
        has_three_vowels(string),
        has_double_letters(string),
        doesnt_have_strings(string)
    ]
    return all(tests)

tests = {
    'ugknbfddgicrmopn': True,
    'aaa': True,
    'jchzalrnumimnmhp': False,
    'haegwjzuvuyypxyu': False,
    'dvszwmarrgswjxmb': False
}
for test, result in tests.items():
    assert is_nice(test) == result
print('is_nice passes tests')

def read_input():
    with open('input_day5.txt') as src:
        words = src.readlines()
        return words

print(sum([int(is_nice(s)) for s in read_input()]))

