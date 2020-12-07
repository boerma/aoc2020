#! /usr/bin/env python

exec(open('_get_data.py').read())

def groups(s):
    return s.split('\n\n')

def members(group):
    return map(set, group.split('\n'))

def yes(group):
    return len(set.intersection(*members(group)))

print(sum(map(yes, groups(data))))
