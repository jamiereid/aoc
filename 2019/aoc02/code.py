# Advent of Code 2019 - Day 2
# Start: 2019-12-09 10:54

import os
import inspect

class IntcodeProgram():
    def __init__(self, tape):
        self.program = tape
        self.programlen = len(self.program)
        self.cursor = 0
        self.icurr = (None, None, None, None)
       # tuple([self.program[self.cursor],
       #                     self.program[self.cursor + 1],
       #                     self.program[self.cursor + 2],
       #                     self.program[self.cursor + 3]])

    def __iter__(self):
        return self

    def __next__(self):
        if (self.cursor + 4) > self.programlen:
            raise StopIteration()

        self.icurr = tuple([self.program[self.cursor],
                            self.program[self.cursor + 1],
                            self.program[self.cursor + 2],
                            self.program[self.cursor + 3]])
        self.cursor = self.cursor + 4
        return self.icurr

    def dump(self):
        return self.program

    def get_register(self, x):
        return self.program[x]

    def set_register(self, x, value):
        self.program[x] = value

    def patch(self, patch):
        for r, v in patch:
            self.set_register(r, v)

    def process_instruction(self, iset, i):
        (o, ae, be, r) = i

        func = iset.get(o, "HALT")
        if func == "HALT": return

        self.set_register(r, func(self.get_register(ae), self.get_register(be)))


def solve_part_one(tape):
    patch = [(1, 12), (2, 2)] # r1=12, r2=2
    p1_iset = {
        1:  (lambda a, b : a + b),
        2:  (lambda a, b : a * b),
        99: "HALT"
    }

    prog = IntcodeProgram(tape)
    prog.patch(patch)

    for instruction in iter(prog):
        prog.process_instruction(p1_iset, instruction)

    return prog.dump()


def solve_part_two(tape):
    answer = []
    return answer


if __name__ == '__main__':
    with open((os.path.abspath(__file__).rstrip('code.py')+'input.txt'),
              'r') as input_file:
        input = input_file.read()
    tape = [int(register) for register in input.split(',')]

    print(f'Part One: {solve_part_one(tape)[0]}')
    print(f'Part Two: {solve_part_two(tape)}')
