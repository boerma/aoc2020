#! /usr/bin/env python

exec(open('_get_data.py').read())

directions = [(1,1), (3,1), (5,1), (7,1), (1,2)]
total = 1
for dx,dy in directions:
    trees = 0
    for i,line in enumerate(data.split('\n')[::dy]):
        if line[(dx*i)%len(line)]=='#':
            trees += 1
    total *= trees

print(total)
print(data.replace('#','🌲').replace('.','❄️'))