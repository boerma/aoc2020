#! /usr/bin/env python

exec(open('_get_data.py').read())

expenses = [int(_) for _ in data.split()]

l = [None]*2020
for e in expenses:
    l[2020-e] = e
    if l[e]:
        print(e*l[e])
