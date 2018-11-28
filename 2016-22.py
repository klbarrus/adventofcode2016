#!/usr/bin/env python3
# AdventOfCode 2016 Day 22

import sys
import re
from collections import namedtuple


def parse_info(line):
    return [int(x) for x in re.findall('\d+', line)]


def viable_node(na, nb):
    return na.used != 0 and na != nb and na.used <= nb.avail


Node = namedtuple('Node', 'x y size used avail percent')
nodelist = []
with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith('/dev'):
            new_node = Node(*parse_info(line))
            nodelist.append(new_node)
f.close()

numv = 0
for a in nodelist:
    for b in nodelist:
        if viable_node(a, b):
            numv += 1
print('part 1: {} viable nodes'.format(numv))

