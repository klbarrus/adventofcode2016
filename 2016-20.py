#!/usr/bin/env python3
# AdventOfCode 2016 Day 20

import sys
import copy


def blocked(addr, fw):
    rv = False
    for i in fw:
        if i[0] <= addr <= i[1]:
            rv = True
            break
    return rv


# read in firewall rules
firewall = []
with open(sys.argv[1]) as f:
    for line in f:
        line = line.rstrip()
        if len(line) > 0:
            lo, hi = line.split('-')
            lo = int(lo)
            hi = int(hi)
            firewall.append((lo, hi))
f.close()

firewall.sort()
print('{} firewall rules'.format(len(firewall)))

# coalesce firewall rules
new_firewall = []
si = 0
while si < len(firewall):
    new_firewall = copy.deepcopy(firewall)
    lo = firewall[si][0]
    hi = firewall[si][1]
    for j in range(si + 1, len(firewall)):
        if firewall[j][0] <= hi + 1:
            if hi < firewall[j][1]:
                hi = firewall[j][1]
        else:
            del new_firewall[si:j]
            new_firewall.insert(si, (lo, hi))
            break
        # max ipaddr reached, check remaining entries for overlap
        if hi >= (2**32 - 1):
            # these entries are ok
            new_firewall = copy.deepcopy(firewall[0:j])
            # check remaining entries for overlap, don't append if there is
            for k in range(j, len(firewall)):
                overlap = False
                for p in range(0, j):
                    if firewall[p][0] <= firewall[k][0] and firewall[k][1] <= firewall[p][1]:
                        overlap = True
                        break
                if not overlap:
                    new_firewall.append(firewall[k])
            firewall = copy.deepcopy(new_firewall)
            break
    si += 1
    firewall = copy.deepcopy(new_firewall)

print('{} firewall rules after coalescing'.format(len(firewall)))
print('')
print('part 1: first address not blocked is {}'.format(firewall[0][1] + 1))

total = 0
for i in range(1, len(firewall)):
    total += firewall[i][0] - firewall[i - 1][0] - 1

print('part 2: {} total addresses not blocked'.format(total))

