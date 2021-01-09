""" Advent of Code day 3 """

import numpy as np
from aocd import get_data
from dotenv import load_dotenv


def day3_1(area, right, down):
    """Count all the trees (#) in area you would encounter for the slope right, down"""
    markers = []
    rows = int(len(area)/down)
    columns = len(area[0])

    for i in range(0, rows):
        # the % operator returns the remainder of the division
        remainder = (right * i) % columns
        marker = area[i * down][remainder]
        markers.append(marker)

    return markers.count('#')


def day3_2(area):
    """Determine the number of trees you would encounter for the following slopes"""
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = []
    for slope in slopes:
        r, d = slope
        count = day3_1(area=area, right=r, down=d)
        trees.append(count)
    print(f"Number of trees on each of the slopes: {trees}")
    return np.prod(trees)


if __name__ == "__main__":
    load_dotenv()

    lines = get_data(day=3, year=2020).splitlines()

    # --- Part One ---
    picture = [list(line) for line in lines]

    count_trees = day3_1(area=picture, right=3, down=1)

    print(f"Part One: We encounter {count_trees} trees")

    # --- Part Two ---
    multiplication = day3_2(area=picture)

    print(f"Part Two: Multiply together the number of trees encountered on each of the listed slopes: {multiplication}")
