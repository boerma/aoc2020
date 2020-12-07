#! /usr/bin/env python

exec(open('_get_data.py').read())

n=0
for line in data.split('\n'):
    lims, target, password = line.split()
    f,t = lims.split('-')
    target = target[:-1]
    if bool(password[int(f)-1]==target) ^ bool(password[int(t)-1]==target):
        n+=1
print(n)
