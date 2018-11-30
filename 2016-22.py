#!/usr/bin/env python3
# AdventOfCode 2016 Day 22

import sys
import re
from collections import namedtuple


def parse_info(line):
    return [int(x) for x in re.findall('\d+', line)]


def viable_node(na, nb):
    return na.used != 0 and na != nb and na.used <= nb.avail


def get_node(x, y, nl):
    return [nodes for nodes in nl if nodes.x == x and nodes.y == y][0]


Node = namedtuple('Node', 'x y size used avail percent')
nodelist = []
with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith('/dev'):
            new_node = Node(*parse_info(line))
            nodelist.append(new_node)
f.close()

numv = sum(viable_node(a, b) for a in nodelist for b in nodelist)
print('part 1: {} viable nodes'.format(numv))

max_x = max(node.x for node in nodelist)
max_y = max(node.y for node in nodelist)
print('grid dimensions: {} x {}'.format(max_x, max_y))
data_start = get_node(max_x, 0, nodelist)
print('data starts at {}'.format(data_start))
zero_start = [nodes for nodes in nodelist if nodes.used == 0][0]
print('empty starts at {}'.format(zero_start))

for x in range(0, max_x + 1):
    row = ''
    for y in range(0, max_y + 1):
        node = get_node(x, y, nodelist)
        if x == 0 and y == 0:
            row += 'G'
        elif x == data_start.x and y == data_start.y:
            row += 'D'
        elif x == zero_start.x and y == zero_start.y:
            row += 'Z'
        elif node.percent >= 85:
            row += '#'
        else:
            row += '.'
    print('{}'.format(row))

            
