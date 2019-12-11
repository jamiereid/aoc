# Advent of Code 2019 - Day 4
# Start: 2019-12-11 19:43

import os


def is_candidate(passwd):
    spasswd = str(passwd)

    # must be six digits (this is not needed really given our input)
    if len(spasswd) != 6:  return False

    # must contain two adjacent digits that are the same
    # left to right must never decrease
    ok = False
    for i in range(len(spasswd) - 1):
        if spasswd[i] == spasswd[i+1]:  ok = True
        if int(spasswd[i]) > int(spasswd[i+1]):
            ok = False
            break
    if not ok:  return False

    return True


def additional_check(passwd):
    spasswd = str(passwd)

    for i in range(len(spasswd) - 1):
        if spasswd[i] * 2 in spasswd and not spasswd[i] * 3 in spasswd:
            return True

    return False


def solve_part_one(input):
    min, max = input[0].split('-')

    meets_criteria = [p for p in range(int(min), int(max)) if is_candidate(p)]

    answer = len(meets_criteria)  # 1665
    return str(answer)


def solve_part_two(input):
    min, max = input[0].split('-')

    meets_criteria = [p for p in range(int(min), int(max))
                      if is_candidate(p) and additional_check(p)]

    answer = len(meets_criteria)  # 1131
    return str(answer)


if __name__ == '__main__':
    with open((os.path.abspath(__file__).rstrip('code.py')+'input.txt'),
              'r') as input_file:
        input = input_file.read()
    input = [line for line in input.splitlines()]

    print(f'Part One: {solve_part_one(input)}')
    print(f'Part Two: {solve_part_two(input)}')
