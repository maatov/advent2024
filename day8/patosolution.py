import re
from itertools import combinations

contents = open("input.txt").readlines()

# Part 1
pattern = "[^.]"
antennas = {}
antinodes = []

for i in range(len(contents)):
    line = contents[i].strip()
    while re.search(pattern, line):
        match = re.search(pattern, line)
        line = line[:match.span()[0]] + '.' + line[match.span()[1]:]
        try:
            antennas[match.group()].append([i, match.span()[0]])
        except KeyError:
            antennas[match.group()] = [[i, match.span()[0]]]

for key, coordinates in antennas.items():
    for start, end in combinations(coordinates, 2):
        distance = [abs(end[0] - start[0]), abs(end[1] - start[1])]

        if start[0] < end[0] and start[1] <= end[1]:
            # Start is above and left (or directly above) relative to End
            antinode = [start[0] - distance[0], start[1] - distance[1]]
            antinode2 = [end[0] + distance[0], end[1] + distance[1]]
        elif start[0] >= end[0] and start[1] <= end[1]:
            # Start is below and left (or directly below) relative to End
            antinode = [end[0] - distance[0], end[1] + distance[1]]
            antinode2 = [start[0] + distance[0], start[1] - distance[1]]
        elif start[0] >= end[0] and start[1] > end[1]:
            # Start is below and right relative to End
            antinode = [end[0] - distance[0], end[1] - distance[1]]
            antinode2 = [start[0] + distance[0], start[1] + distance[1]]
        elif start[0] < end[0] and start[1] > end[1]:
            # Start is above and right relative to End
            antinode = [start[0] - distance[0], start[1] + distance[1]]
            antinode2 = [end[0] + distance[0], end[1] - distance[1]]
        else:
            # Default catch-all case for any unhandled scenarios
            antinode = [end[0] + distance[0], end[1] + distance[1]]
            antinode2 = [start[0] - distance[0], start[1] - distance[1]]

        for node in [antinode, antinode2]:
            if 0 <= node[0] < len(contents) and 0 <= node[1] < len(contents[0].strip()):
                if node not in antinodes:
                    antinodes.append(node)

print(len(antinodes))