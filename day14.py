""" Advent of Code day 14 """

from dotenv import load_dotenv
from aocd.models import Puzzle
import itertools
import re


def bit36(i: int) -> str:
    return f'{i:036b}'


def parse_docking(line: str) -> tuple:
    """Parse 'mask = XX10' to ('mask', 'XX10') and 'mem[8] = 11' to (8, 11)"""
    if line.startswith('mask'):
        return 'mask', line.split()[-1]
    else:
        return tuple(map(int, re.findall(r'\d+', line)))


def day14_1(data):
    programs = [parse_docking(i) for i in data]
    results = {}
    for program in programs:
        addr, val = program
        if addr == "mask":
            mask = val
        else:
            result = [j if i == "X" else i for i, j in zip(mask, bit36(val))]
            results[f"mem[{addr}]"] = int("".join(result), 2)

    print(f"Part 1: Sum of all values left in memory after completion: {sum(results.values())}")

    return sum(results.values())


def day14_2(data):
    programs = [parse_docking(i) for i in data]
    print(programs)
    results = {}
    for program in programs:
        addr, val = program
        memory_addresses = []

        if addr == "mask":
            mask = val
            nr_bitmask_bit_x = list(mask).count('X')
            print(f"Mask contains {nr_bitmask_bit_x} floating points, causing writes to {2 ** nr_bitmask_bit_x} addresses")

            # the floating bits will take on all possible values
            a = [["0", "1"]] * nr_bitmask_bit_x
            floating_bits = list(itertools.product(*a))

            indices_bitmask_bit_x = [ind for ind, i in enumerate(mask) if i == "X"]
        else:
            # If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
            value_bit_list = [i if i == "1" else j for i, j in zip(mask, bit36(addr))]
            value_bit = "".join(value_bit_list)

            # If the bitmask bit is X, the corresponding memory address bit is floating.
            for b in floating_bits:
                result = list(value_bit)
                for ind, mask_ind in enumerate(indices_bitmask_bit_x):
                    result[mask_ind] = b[ind]
                memory_addresses.append("".join(result))

        memory_addresses = [int(s, 2) for s in memory_addresses]

        for i in memory_addresses:
            print(f"mem[{i}]: {val}")
            results[f"mem[{i}]"] = val

    print(f"Part 2: Sum of all values left in memory after completion: {sum(results.values())}")

    return sum(results.values())


if __name__ == "__main__":
    load_dotenv()

    puzzle = Puzzle(year=2020, day=14)
    input_data = puzzle.input_data.splitlines()
    day14_1(data=input_data)
    day14_2(data=input_data)
