""" Advent of Code day 15 """

from dotenv import load_dotenv
from aocd.models import Puzzle


def day15(data, threshold=2020):
    # Uses a dictionary to find the number spoken
    turn = len(data)
    d = {int(val): {"turn": [ind], "count": 1} for ind, val in enumerate(data)}
    last_value = int(data[-1])

    while turn != threshold:
        # Time complexity of looking up a value in dictionary is O(1)
        if d[last_value]["count"] == 1:
            new_value = 0
            # Time complexity is O(1)
            if new_value in d:
                d[new_value]["turn"].append(turn)
                d[new_value]["count"] += 1
            else:
                d[new_value] = {"turn": [turn], "count": 1}
        else:
            new_value = d[last_value]["turn"][-1] - d[last_value]["turn"][-2]
            if new_value in d:
                d[new_value]["turn"].append(turn)
                d[new_value]["count"] += 1
            else:
                d[new_value] = {"turn": [turn], "count": 1}
        turn += 1
        last_value = new_value

    print(f"Given {','.join(data)} the {threshold}th number spoken is {last_value}")
    return last_value


if __name__ == "__main__":
    load_dotenv()

    puzzle = Puzzle(year=2020, day=15)
    input_data = puzzle.input_data.split(",")
    day15(data=input_data, threshold=2020)
    day15(data=input_data, threshold=30000000)

