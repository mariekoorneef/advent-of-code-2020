""" Advent of Code day 8 """

from aocd import get_data
from dotenv import load_dotenv


def parse_instruction(instruction: str) -> tuple:
    """Given 'acc +1' return (acc, 1)"""
    return instruction[:3], int(instruction[4:])


def execute_instruction(instruction: tuple, acc: int, i: int) -> tuple:
    """Execute instructions"""
    if instruction[0] == "acc":
        i += 1
        acc += instruction[1]
    elif instruction[0] == "jmp":
        i += instruction[1]
    elif instruction[0] == "nop":
        i += 1
    # print(i, accumulator)
    return i, acc


def modify_list(l: list, index: int, new_value: tuple) -> list:
    """Replace list index with new_value"""
    l2 = l.copy()
    l2[index] = new_value
    return l2


def modify_tuple(t: tuple) -> tuple:
    """Given (jmp, 4) return (nop, 4)"""
    if t[0] == "jmp":
        return "nop", t[1]
    elif t[0] == "nop":
        return "jmp", t[1]


def part_2(l: list, v: list, i: int = 0, acc: int = 0) -> tuple:
    visit = v.copy()
    while i < len(visit) and visit[i] == 0:
        visit[i] = 1
        i, acc = execute_instruction(instruction=l[i], acc=acc, i=i)

    if i == len(visit):
        # The program is supposed to terminate by attempting to execute an instruction
        # immediately after the last instruction in the file
        return acc, True
    else:
        return acc, False


def day8_1(data):
    """Execute the program until it loops; then return accum. """
    instructions = [parse_instruction(i) for i in data]

    visit = [0]*len(data)
    i = accumulator = 0

    while visit[i] == 0:
        visit[i] = 1
        i, accumulator = execute_instruction(instruction=instructions[i], acc=accumulator, i=i)

    return accumulator


def day8_2(data):
    """By changing exactly one jmp or nop, the code terminates correctly."""
    visit = [0] * len(data)
    instructions = [parse_instruction(i) for i in data]
    i = accumulator = 0

    # Run the program until it loops or terminates; return (terminates, accum)
    while visit[i] == 0:
        if instructions[i][0] in ("jmp", "nop"):
            # By changing exactly one jmp or nop, check if the code terminates correctly (boolean)
            m = modify_tuple(t=instructions[i])
            l = modify_list(l=instructions, index=i, new_value=m)
            accumulator_final, boolean = part_2(l=l, v=visit, i=i, acc=accumulator)
            if boolean:
                break

        visit[i] = 1
        i, accumulator = execute_instruction(instruction=instructions[i], acc=accumulator, i=i)

    return accumulator_final


if __name__ == "__main__":
    load_dotenv()

    input_data = get_data(day=8, year=2020).splitlines()

    # --- Part One ---
    print(f"Part One: Immediately before any instruction is executed a second time, the value in the accumulator is {day8_1(data=input_data)}.")

    # --- Part Two ---
    print(f"Part Two: The value of the accumulator after the program terminates: {day8_2(data=input_data)}")
