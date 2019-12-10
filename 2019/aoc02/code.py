# Advent of Code 2019 - Day 2
# Start: 2019-12-09 10:54

import os
import inspect

class IntcodeComputer():
    def __init__(self, instruction_set):
        self._memory = []
        self._instruction_set = instruction_set
        self._maxmemsize = len(self._memory)
        self._memptr = 0

        self._current_inst = (None, None, None, None)

    # @Todo: abstract memory out - it makes more sense to iterate over memory
    #        addresses than it does to iterate over a computer
    def __iter__(self):
        return self

    def __next__(self):
        if (self._memptr + 4) > self._maxmemsize:
            raise StopIteration()

        self._current_inst = tuple([self._memory[self._memptr],
                                    self._memory[self._memptr + 1],
                                    self._memory[self._memptr + 2],
                                    self._memory[self._memptr + 3]])
        self._memptr += 4
        return self._current_inst

    def memdump(self):
        return self._memory

    def readaddr(self, addr):
        return self._memory[addr]

    def wraddr(self, addr, value):
        self._memory[addr] = value

    def memload(self, tape):
        self._memory = tape
        self._maxmemsize = len(self._memory)

    def mempatch(self, patch):
        for addr, value in patch:
            self.wraddr(addr, value)

    def setpointer(self, addr):
        self._mempointer = addr

    def run(self):
        for inst in iter(self):
            self._do_instruction(inst)

    def step(self):
        inst = tuple([self._memory[self._memptr],
                      self._memory[self._memptr + 1],
                      self._memory[self._memptr + 2],
                      self._memory[self._memptr + 3]])
        self._memptr += 4
        self._do_instruction(inst)

    def _do_instruction(self, inst):
        (opcode, a_addr, b_addr, r_addr) = inst

        func = self._instruction_set.get(opcode, "HALT")
        if func == "HALT": return

        self.wraddr(r_addr, func(self.readaddr(a_addr), self.readaddr(b_addr)))


def solve_part_one(tape, do_patch = False):
    patch = [(1, 12), (2, 2)] # r1=12, r2=2
    p1_iset = {
        1:  (lambda a, b : a + b),
        2:  (lambda a, b : a * b),
        99: "HALT"
    }

    comp = IntcodeComputer(p1_iset)
    comp.memload(tape)
    if do_patch:  comp.mempatch(patch)
    comp.setpointer(0)
    comp.run()

    return comp.memdump()


def solve_part_two(tape):
    answer = []
    return answer


if __name__ == '__main__':
    with open((os.path.abspath(__file__).rstrip('code.py')+'input.txt'),
              'r') as input_file:
        input = input_file.read()
    tape = [int(register) for register in input.split(',')]

    print(f'Part One: {solve_part_one(tape, True)[0]}')
    print(f'Part Two: {solve_part_two(tape)}')
