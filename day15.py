""" Advent of Code day 15 """

from dotenv import load_dotenv
from aocd.models import Puzzle
from helper import data


def day15(text, nth=2020):
    """Given the starting numbers data, what will be the nth number spoken? """
    numbers = data(text=text, parser=int, sep=",")
    # Uses a dictionary to find the number spoken
    d = {int(val): ind for ind, val in enumerate(numbers[:-1])}
    last_value = int(numbers[-1])

    for turn in range(len(numbers), nth):
        # Time complexity of looking up a value in dictionary is O(1)
        if last_value in d:
            new_value = turn - 1 - d[last_value]
        else:
            new_value = 0
        d[last_value] = turn - 1
        last_value = new_value

    print(f"Given {text} the {nth}th number spoken is {last_value}")
    return last_value


if __name__ == "__main__":
    load_dotenv()

    puzzle = Puzzle(year=2020, day=15)
    day15(text=puzzle.input_data, nth=2020)
    day15(text=puzzle.input_data, nth=30000000)
