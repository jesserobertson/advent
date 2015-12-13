#!/usr/bin/env python

from hashlib import md5

tests = ['abcdef', 'pqrstuv']

string = 'iwrupvqb'
for idx in range(10000000):
    hash = md5((string + str(idx)).encode('ascii'))
    if hash.hexdigest().startswith('000000'):
        print(idx)
        break

