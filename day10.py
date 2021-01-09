""" Advent of Code day 10 """

from collections import Counter
import numpy as np
from aocd import get_data
from dotenv import load_dotenv
from collections.abc import Iterable


def create_children(input_list: list, parents: list) -> dict:
    """Create a parent child dictionary tree,
     e.g. input_list [0, 1, 2] returns {0: {1: {2: {}}, 2: {}}}"""
    tree = {}
    if not isinstance(parents, list) and not parents:
        return tree

    for parent in parents:
        ind = input_list.index(parent)
        possible_children = set(range(parent + 1, parent + 4))
        children = set(input_list[ind:]).intersection(possible_children)
        tree[parent] = create_children(input_list, children)
    return tree


def paths(tree: dict, cur: tuple = ()) -> Iterable:
    """Generate all leaf to root paths in a dictionary tree in python"""
    if not tree:
        yield cur
    else:
        for key, value in tree.items():
            for path in paths(value, cur+(key,)):
                yield path


def calculate_nr_paths_tree(list_length):
    """ Given a  contiguous sets with list_length, calculate the number of distinct paths
     e.g. for list_length 3 - input_list [1, 2, 3] - the number of paths is 2 """
    input_list = list(range(0, list_length))
    # print(f"Input: {input_list}")
    tree = create_children(input_list=input_list, parents=[input_list[0]])
    tree_paths = list(paths(tree))
    # print(f"Distinct paths {tree_paths}")
    nr_paths = len(tree_paths)
    # print(f"Total number of distinct paths {nr_paths}")
    return nr_paths


def day10_1(data):
    numbers = sorted([int(i) for i in data])
    device_joltage = max(numbers) + 3
    joltages = [0] + numbers + [device_joltage]
    result = [y - x for x, y in zip(joltages[:-1], joltages[1:])]
    jolt_count = dict(Counter(result).items())

    print("Part One:")
    for jolt in jolt_count.keys():
        print(f"\t The input has {jolt_count[jolt]} {jolt}-jolt differences")

    print(f"The number of 1-jolt differences multiplied by the number of 3-jolt differences:"
          f" {jolt_count[1]*jolt_count[3]}\n")
    return jolt_count[1], jolt_count[3]


def day10_2(data):
    numbers = sorted([int(i) for i in data])
    device_joltage = max(numbers) + 3
    joltages = [0] + numbers + [device_joltage]
    result = [y - x for x, y in zip(joltages[:-1], joltages[1:])]
    indices = [0] + [i + 1 for i, x in enumerate(result) if x == 3]

    print("Part Two: When a 3-jolt difference occurs, we split the list in two lists.")

    # When split on 3-jolt differences, the lists has length 1, 2, 3, 4, 5
    mapping = {1: 1, 2: 1}
    for i in [3, 4, 5]:
        mapping[i] = calculate_nr_paths_tree(list_length=i)

    arrangements = []
    len_sublist = []

    for i, index in enumerate(indices[:-1]):
        sublist = joltages[index:indices[i + 1]]
        j = len(sublist)
        len_sublist.append(j)
        arrangements.append(mapping[j])

    nr_distinct_arrangements = np.prod(arrangements)

    print(f"The unique lengths of the contiguous sets are:"
          f" {sorted(list(set(len_sublist)))}")
    print(f"\t A contiguous set with length 5, e.g. {list(range(0, 5))}, "
          f"has {mapping[5]} distinct arrangements.")
    # print(len_sublist)
    # print(arrangements)
    print(f"Part Two: The total number of distinct ways I can arrange "
          f"the adapters to connect the charging outlet"
          f" to your my device {nr_distinct_arrangements}")

    return nr_distinct_arrangements


if __name__ == "__main__":
    load_dotenv()

    lines = get_data(day=10, year=2020).splitlines()

    # --- Part One ---
    day10_1(data=lines)

    # --- Part Two ---
    day10_2(data=lines)
