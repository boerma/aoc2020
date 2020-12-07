#! /usr/bin/env python

exec(open('_get_data.py').read())

expenses = [int(_) for _ in data.split()]

for e1 in expenses:
    for e2 in expenses:
        for e3 in expenses:
            if e1+e2+e3==2020:
                print(e1*e2*e3)
                exit()
