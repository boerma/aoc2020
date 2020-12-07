#! /usr/bin/env python

data = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

exec(open('_get_data.py').read())

def parse(i):
    d = dict()
    for line in i.split('.\n'):
        if not line:
            continue
        part = line.split(' bags contain ')
        d[part[0]] = parse_rule(part[1])
    return d

def parse_rule(line):
    d = dict()
    for part in line.replace('.', '').split(', '):
        num, *bags = part.split(' ')
        bags = ' '.join(bags[:-1])
        try:
            d[bags] = int(num)
        except ValueError:
            if num=='no':
                pass
            else:
                print(part)
                raise
    return d

def can_contain(bag):
    return (r for r  in rules if bag in rules[r])

def find(target):
    r = [target]
    for container in can_contain(target):
        r.extend(find(container))
    return r

rules = parse(data)

print(len(set(find('shiny gold')))-1)
