# Advent of Code 2019 - Day 01
# Start: datetime

import os
from math import floor

def calculate_fuel(mass):
    return floor(mass / 3) - 2


def r_calculate_fuel(mass):
    fuel = max(calculate_fuel(mass), 0)

    if fuel == 0: return 0
    return fuel + r_calculate_fuel(fuel)


def solve_part_one(intput):
    answer = sum(list(map(calculate_fuel, intput)))
    return str(answer)


def solve_part_two(intput):
    answer = sum([r_calculate_fuel(mod) for mod in intput])
    return str(answer)


if __name__ == '__main__':
    with open((os.path.abspath(__file__).rstrip('code.py')+'input.txt'),
              'r') as input_file:
        input = input_file.read()
    intput = [int(line) for line in input.splitlines()]

    print(f'Part One: {solve_part_one(intput)}')
    print(f'Part Two: {solve_part_two(intput)}')
