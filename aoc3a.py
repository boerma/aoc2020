#! /usr/bin/env python

exec(open('_get_data.py').read())

trees = 0
for i,line in enumerate(data.split('\n')):
    if line[(3*i)%len(line)]=='#':
        trees += 1

print(trees)
