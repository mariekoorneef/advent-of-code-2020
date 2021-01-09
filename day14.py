""" Advent of Code day 14 """

from dotenv import load_dotenv
from aocd.models import Puzzle
import itertools


def day14_1(data):
    programs = [i.split(" = ") for i in data]
    print(programs)
    results = {}
    for program in programs:
        if program[0] == "mask":
            mask = program[1]
        else:
            value = int(program[1])
            value_bit = f"{value:036b}"
            result = []
            for i, j in zip(mask, value_bit):
                if i == "X":
                    result.append(j)
                else:
                    result.append(i)

            result_string = "".join(result)
            results[program[0]] = int(result_string, 2)

    print(f"Part 1: Sum of all values left in memory after completion: {sum(results.values())}")

    return sum(results.values())


def day14_2(data):
    programs = [i.split(" = ") for i in data]
    print(programs)
    results = {}
    for program in programs:
        memory_addresses = []

        if program[0] == "mask":
            mask = program[1]
            nr_bitmask_bit_x = list(mask).count('X')
            nr_memory_addresses = 2 ** nr_bitmask_bit_x
            print(f"Mask contains {nr_bitmask_bit_x} floating points, causing writes to {nr_memory_addresses} addresses")

            # the floating bits will take on all possible values
            a = [["0", "1"]] * nr_bitmask_bit_x
            floating_bits = list(itertools.product(*a))

            indices_bitmask_bit_x = [ind for ind, i in enumerate(mask) if i == "X"]
            indices_bitmask_bit_1 = [ind for ind, i in enumerate(mask) if i == "1"]
        else:
            memory_address = int(program[0].replace("mem[", "").replace("]", ""))
            value_bit = f"{memory_address:036b}"
            value_bit_list = list(value_bit)

            # If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
            for ind in indices_bitmask_bit_1:
                value_bit_list[ind] = "1"

            value_bit = "".join(value_bit_list)

            # If the bitmask bit is X, the corresponding memory address bit is floating.
            for b in floating_bits:
                result = list(value_bit)
                for ind, mask_ind in enumerate(indices_bitmask_bit_x):
                    result[mask_ind] = b[ind]
                memory_addresses.append("".join(result))

        memory_addresses = [int(s, 2) for s in memory_addresses]

        for i in memory_addresses:
            print(f"mem[{i}]: {program[1]}")
            results[f"mem[{i}]"] = int(program[1])

    print(f"Part 2: Sum of all values left in memory after completion: {sum(results.values())}")

    return sum(results.values())


if __name__ == "__main__":
    load_dotenv()

    puzzle = Puzzle(year=2020, day=14)
    input_data = puzzle.input_data.splitlines()
    day14_1(data=input_data)
    day14_2(data=input_data)
