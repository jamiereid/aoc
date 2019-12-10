# Advent of Code 2019 - Day X
# Start: datetime

import os
import svgwrite


CSS = """
    .grid { stroke: firebrick; stroke-width: .1mm; }
    .background { fill: black; }
"""

def group(drawobj, grpname):
    return drawobj.add(drawobj.g(class_=grpname))

def visualise():
    outfile = 'part_one.svg'
    grid_squared = 10
    viewbox_max = 80
    world_size=("10cm", "10cm")
    unit = int(world_size[0].replace('cm','')) / viewbox_max

    dwg = svgwrite.Drawing(outfile, size=world_size)
    dwg.viewbox(0, 0, viewbox_max, viewbox_max)
    dwg.defs.add(dwg.style(CSS))

    dwg.add(dwg.rect(size=("100%", "100%"), class_='background'))

    # Draw grid
    lines = group(dwg, "grid")
    for i in range(grid_squared - 1):
        y = i * grid_squared
        lines.add(dwg.line(start=(0, y), end=(viewbox_max, y)))
        x = i * grid_squared
        lines.add(dwg.line(start=(x, 0), end=(x, viewbox_max)))

    dwg.save()

def solve_part_one(input):
    # input is array of array of line instructions
    move = {'U': "u",
            'D': "d",
            'L': "l",
            'R': "r"}

    print(input)
    print(f'type={type(input[0])}')

    # YOU WERE TIRED. YOU HAVE NOT SPLIT ON , YET.

    def do(x):
        action = move[x[0]]
        amount = x[1:]
        print(f'action:{action}, amount:{amount}')

    [do(x) for x in input[0]]

    answer = 0
    return str(answer)


def solve_part_two(input):
    answer = 0
    return str(answer)


if __name__ == '__main__':
    with open((os.path.abspath(__file__).rstrip('code.py')+'input.txt'),
              'r') as input_file:
        input = input_file.read()
    ins = [[line] for line in input.splitlines()]

    print(f'Part One: {solve_part_one(ins)}')
    print(f'Part Two: {solve_part_two(ins)}')
