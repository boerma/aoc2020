#! /usr/bin/env python

exec(open('_get_data.py').read())

def groups(s):
    return s.split('\n\n')

def yes(group):
    return len(set(group.replace('\n', '')))

print(sum(map(yes, groups(data))))
