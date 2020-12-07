#! /usr/bin/env python

exec(open('_get_data.py').read())

def seat_id_str(s):
    return s.translate(str.maketrans('BFRL','1010'))

seat_ids = set(int(_, base=2) for _ in seat_id_str(data).split())
seat, = set(range(min(seat_ids),max(seat_ids))) - seat_ids
print(seat)

from random import shuffle
data = list(range(31,128))
del data[57]
shuffle(data)

seat, lo, hi = 0, 0, 127
for _ in data:
    seat^=_
print(seat)
