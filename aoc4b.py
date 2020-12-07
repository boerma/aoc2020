#! /usr/bin/env python

exec(open('_get_data.py').read())

import re

def parse(pp_str):
  return {key: val for field in pp_str.split() for key, val in [field.split(':')]}

def valid(pp):
  check = {
    'byr': lambda s: re.match('^[0-9]{4}$', s) and 1919<=int(s)<=2002,
    'iyr': lambda s: re.match('^[0-9]{4}$', s) and 2010<=int(s)<=2020,
    'eyr': lambda s: re.match('^[0-9]{4}$', s) and 2020<=int(s)<=2030,
    'hgt': lambda s: re.match('^[0-9]+..$', s) and ((s[-2:]=='in' and 59<=int(s[:-2])<=76) or (s[-2:]=='cm' and 150<=int(s[:-2])<=193)),
    'hcl': lambda s: re.match('^#[0-9a-f]{6}$', s),
    'ecl': lambda s: s in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda s: re.match('^[0-9]{9}$', s),
    'cid': lambda s: True,
  }
  del check['cid']
  return all(f in pp and check[f](pp[f]) for f in check)

passports = map(parse, data.split('\n\n'))
print(sum(map(valid, passports)))
