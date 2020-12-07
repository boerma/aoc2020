#! /usr/bin/env python

exec(open('_get_data.py').read())

def parsepp(s):
	return {key: val for field in s.split() for key, val in [field.split(':')]}

def valid(pp):
	fields = 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'
	return all(f in pp for f in set(fields)-set(['cid']))

passport = [parsepp(pp) for pp in data.split('\n\n')]
print(sum(valid(pp) for pp in passport))
