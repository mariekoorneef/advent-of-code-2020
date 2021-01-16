from helper import data
import scipy.signal
import numpy as np
from typing import List
from dotenv import load_dotenv
from aocd.models import Puzzle


def parse_state(text: str) -> List[int]:
    """parse active '#' to 1 and inactive '.' to 0"""
    def f(x):
        if x == ".":
            return 0
        else:
            return 1
    return list(map(f, list(text)))


def remove_zero_borders(a):
    """Remove zero borders of 3D or 4D array"""
    d = len(a.shape)
    if d == 3:
        xs, ys, zs = np.where(a != 0.0)
        return a[min(xs):max(xs) + 1, min(ys):max(ys) + 1, min(zs):max(zs) + 1]
    elif d == 4:
        xs, ys, zs, ws = np.where(a != 0.0)
        return a[min(xs):max(xs) + 1, min(ys):max(ys) + 1, min(zs):max(zs) + 1, min(ws):max(ws) + 1]


def execute_cycle(a, kernel):
    """During a cycle, all cubes simultaneously change according to rules"""
    active_neighbors = scipy.signal.convolve(a, kernel, mode="same").round(decimals=0)

    mask = np.isin(active_neighbors, [2, 3], invert=True)
    rule1 = list(zip(*np.where(mask)))
    rule2 = list(zip(*np.where(active_neighbors == 3)))

    # If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active.
    # Otherwise, the cube becomes inactive.
    for cell in rule1:
        if a[cell] == 1:
            a[cell] = 0

    # If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active.
    # Otherwise, the cube remains inactive.
    for cell in rule2:
        if a[cell] == 0:
            a[cell] = 1

    a = remove_zero_borders(a)
    return a


def day17_1(picture, d=3, n=6):
    """How many cubes are left in the active state after nth cycle?"""
    # Part 1: arr is 3-dimensional with coordinates (x,y,z)
    arr_2d = np.array(picture)
    if d == 3:
        arr = arr_2d[..., np.newaxis]
    elif d == 4:
        arr = arr_2d[..., np.newaxis, np.newaxis]
    else:
        return None
    kernel = np.ones((3,)*d)
    kernel[(1,)*d] = 0.0

    for c in range(0, n):
        arr = np.pad(arr, 1, 'constant', constant_values=0.0)
        arr = execute_cycle(a=arr, kernel=kernel)
        print(f"For cycle {c+1}: the sum is {np.sum(arr)} and shape: {arr.shape}")

    return np.sum(arr)


def day17_2(picture): return day17_1(picture, d=4)


if __name__ == "__main__":
    #  active (#) or inactive (.)
    load_dotenv()

    puzzle = Puzzle(year=2020, day=17)
    p = puzzle.input_data

    input_data = data(p, parser=parse_state, sep="\n")

    print(f"Part One:")
    day17_1(input_data)

    print("\nPart Two:")
    day17_2(input_data)
