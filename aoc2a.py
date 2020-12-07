#! /usr/bin/env python

exec(open('_get_data.py').read())

n=0
for line in data.split('\n'):
    try:
        lims, target, password = line.split()
    except ValueError:
        print(line)
        raise
    f,t = lims.split('-')
    target = target[:-1]
    if int(f)<=password.count(target) and password.count(target)<=int(t):
        n+=1
print(n)
