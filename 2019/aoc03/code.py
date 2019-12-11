# Advent of Code 2019 - Day 3
# Start: 2019-12-11 08:54

import os

class Point():
    def __init__(self, x, y):
        self.px = x
        self.py = y

    @property
    def x(self):
        return self.px

    @property
    def y(self):
        return self.py

    def distance_to_origin(self):
        return abs(self.px) + abs(self.py)

    def __str__(self):
        return '({}, {})'.format(self.px, self.py)

    def __repr__(self):
        return 'Point({}, {})'.format(self.px, self.py)

    def __add__(self, other):
        return Point(self.px + other.x, self.py + other.y)

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return ((self.px == other.x) and (self.py == other.y))
        else:
            return False


def process(input):
    direction = {'U': Point(1, 0),
                 'R': Point(0, 1),
                 'D': Point(-1, 0),
                 'L': Point(0, -1)}

    origin = Point(0,0)
    instructions = {k:[{'vector': direction[i[0]], 'amount': int(i[1:])} for i in line.split(',')]
                    for k, line in enumerate(input.splitlines())}
    wires = {k:[origin] for k in range(len(input.splitlines()))}

    # Build a list of Points for each wire
    for i, wire in wires.items():
        for inst in instructions[i]:
            for x in range(inst['amount']):
                cc = wire[-1]  # current coord
                #print(f'cc: {cc}, append: {cc+inst["vector"]}')
                wire.append(cc + inst['vector'])

    # Build a list of intersections
    tmpset = set(wires[1])
    intersections = [i for i in wires[0] if i in tmpset and i != origin]  # @Hardcoded: assumes only two wires

    return wires, intersections


def solve_part_one(input):
    wires, intersections = input

    # Find closest intersection to origin
    md = [i.distance_to_origin() for i in intersections]
    answer = min(md)

    return str(answer)


def solve_part_two(input):
    wires, intersections = input

    steps = {}
    c = 0
    for i, wire in wires.items():
        for point in wire:
            c += 1
            if point in intersections:

                # if we've already recorded a visit continue
                if repr(point) in steps:
                    if i in steps[repr(point)]:
                        continue
                else:
                    steps[repr(point)] = {}

                steps[repr(point)][i] = c
                c = 0

    #totals = [p[0][1] + p[1][1] for p in steps.values()]  # @Hardcoded: assumes only two wires.
    totals = [p[0] + p[1] for p in steps.values()]  # @Hardcoded: assumes only two wires.
    print(steps)

    print(totals)
    answer = min(totals)

    #answer =0
    return str(answer)


if __name__ == '__main__':
    with open((os.path.abspath(__file__).rstrip('code.py')+'input.txt'),
              'r') as input_file:
        input = process(input_file.read())

    print(f'Part One: {solve_part_one(input)}')
    print(f'Part Two: {solve_part_two(input)}')
