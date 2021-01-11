""" Advent of Code day 15 """

from dotenv import load_dotenv
from aocd.models import Puzzle


def day15(data, nth=2020):
    """Given the starting numbers daya, what will be the nth number spoken? """
    # Uses a dictionary to find the number spoken
    d = {int(val): ind for ind, val in enumerate(data[:-1])}
    last_value = int(data[-1])

    for turn in range(len(data), nth):
        # Time complexity of looking up a value in dictionary is O(1)
        if last_value in d:
            new_value = turn - 1 - d[last_value]
        else:
            new_value = 0
        d[last_value] = turn - 1
        last_value = new_value

    print(f"Given {','.join(data)} the {nth}th number spoken is {last_value}")
    return last_value


if __name__ == "__main__":
    load_dotenv()

    puzzle = Puzzle(year=2020, day=15)
    input_data = puzzle.input_data.split(",")
    day15(data=input_data, nth=2020)
    day15(data=input_data, nth=30000000)

