#! /usr/bin/env python

exec(open('_get_data.py').read())

def seat_id_str(s):
    return s.translate(str.maketrans('BFRL','1010'))

print(max(int(_, base=2) for _ in seat_id_str(data).split()))
