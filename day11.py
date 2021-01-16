""" Advent of Code day 11 """

from dotenv import load_dotenv
from aocd.models import Puzzle
import numpy as np
from itertools import product
from collections.abc import Iterable

from helper import lines


def get_neighbours(cell: tuple, size: tuple) -> Iterable:
    """ Get cell index for neighbors in 2d-list: where neighbors are the eight immediately adjacent seats"""
    for c in product(*(range(n-1, n+2) for n in cell)):
        if c != cell and all(0 <= n < s for n, s in zip(c, size)):
            yield c


def get_all_diagonals(a: np.int64) -> list:
    """ Get all the diagonals in a 2d numpy array"""
    diags = [a[::-1, :].diagonal(i) for i in range(-a.shape[0] + 1, a.shape[1])]
    diags.extend(a.diagonal(i) for i in range(a.shape[1] - 1, -a.shape[0], -1))
    return diags


def get_vertical_seats(locations: list, y: int, d: dict) -> dict:
    """ Get all the vertical seats in column y"""
    for i in range(0, y):
        vertical = [loc for loc in locations if loc[1] == i]
        for ind, j in enumerate(vertical):
            d[j].extend(vertical[ind - 1:ind] + vertical[ind + 1:ind + 2])
    return d


def get_horizontal_seats(locations: list, x: int, d: dict) -> dict:
    """ Get all the horizontal seats in row x"""
    for i in range(0, x):
        horizontal = [loc for loc in locations if loc[0] == i]
        for ind, j in enumerate(horizontal):
            d[j].extend(horizontal[ind - 1:ind] + horizontal[ind + 1:ind + 2])
    return d


def get_diagonal_seats(x: int, y: int, layout: np.unicode_, d: dict) -> dict:
    """ Get all diagonal seats """
    # create a default array of specified dimensions
    a = np.arange(x * y).reshape(x, y)

    def f(c):
        if c == "L":
            return 1
        elif c == ".":
            return -1

    # all floor locations are negative
    transformer = np.array([f(cell) for row in layout for cell in row]).reshape(x, y)
    new_a = a*transformer
    if new_a[0, 0] == ".":
        new_a[0, 0] = -1

    diags = get_all_diagonals(new_a)
    for diag in diags:
        # only keep the elements of a diagonal that are positive
        # transform number into cell
        s = [(nr // y, nr % y) for nr in diag if nr > -1]
        for ind, cell in enumerate(s):
            d[cell].extend(s[ind - 1:ind] + s[ind + 1:ind + 2])

    return d


def get_neighbors_part2(locations: list, x: int, y: int, layout: np.unicode_, d: dict) -> dict:
    """For each key seat, get a list of all the first seat a person can see in each of the eight direction"""
    d = get_horizontal_seats(locations=locations, x=x, d=d)
    d = get_vertical_seats(locations=locations, y=y, d=d)
    d = get_diagonal_seats(x=x, y=y, layout=layout, d=d)
    return d


def occupation_of_seats(layout: np.unicode_, d: dict, threshold: int):
    """

    :param layout: seat layout of waiting area
    :param d: dictionary: for each seat ("L" or "#") cell in area a list of neighbors
    :param threshold: nr of visible occupied seats for an occupied seat to become empty
    :return:
    """
    c = layout.copy()
    for key, value in d.items():
        count_occupied = [layout[i] for i in value].count("#")
        if layout[key] == "L" and count_occupied == 0:
            c[key] = "#"
        elif layout[key] == "#" and count_occupied > threshold:
            c[key] = "L"
    if (c == layout).all():
        return c

    # print(c)

    return occupation_of_seats(layout=c, d=d, threshold=threshold)


def day11_1(text):
    # create a numpy array
    picture = np.array([list(line) for line in lines(text)])
    # get indices from the seat locations
    seat_locations = list(zip(*np.where(picture == "L")))

    # create dictionary neigbours
    dict_neighbours = {}
    for s in seat_locations:
        dict_neighbours[s] = list(get_neighbours(cell=s, size=picture.shape))

    final_seating_arrangement = occupation_of_seats(layout=picture, d=dict_neighbours, threshold=3)

    unique, counts = np.unique(final_seating_arrangement, return_counts=True)

    nr_occupied_seats = dict(zip(unique, counts))['#']

    return nr_occupied_seats


def day11_2(text):
    # create a numpy array
    picture = np.array([list(line) for line in lines(text)])
    rows, columns = picture.shape
    # get indices from the seat locations
    seat_locations = list(zip(*np.where(picture == "L")))

    # create dictionary neighbours
    dict_neighbours = {c: [] for c in seat_locations}

    dict_neighbours = get_neighbors_part2(locations=seat_locations, x=rows, y=columns, layout=picture,
                                          d=dict_neighbours)

    final_seating_arrangement = occupation_of_seats(layout=picture, d=dict_neighbours, threshold=4)

    unique, counts = np.unique(final_seating_arrangement, return_counts=True)

    nr_occupied_seats = dict(zip(unique, counts))['#']

    return nr_occupied_seats


if __name__ == "__main__":
    load_dotenv()

    puzzle = Puzzle(year=2020, day=11)
    input_data = puzzle.input_data

    print(f"Part 1: {day11_1(text=input_data)} seats end up occupied")

    print(f"Part 2: {day11_2(text=input_data)} seats end up occupied")
