# Advent of Code 2021 - Day 1

import os

def solve_part_one(intput):
    answer = 0
    for i, v in enumerate(intput):
        if v > intput[i-1]:  answer += 1
    return str(answer)


def solve_part_two(intput):
    answer = 0
    for i, v in enumerate(intput):
        if i + 3 > len(intput):  break

        a = intput[i:i+3]
        b = intput[i+1:i+4]

        if sum(b) > sum(a):  answer += 1
    return str(answer)


if __name__ == '__main__':
    with open((os.path.abspath(__file__).rstrip('code.py')+'input.txt'), 'r') as input_file:
        input = input_file.read()
    intput = [int(line) for line in input.splitlines()]

    print(f'Part One: {solve_part_one(intput)}')
    print(f'Part Two: {solve_part_two(intput)}')
