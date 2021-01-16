""" Advent of Code day 10 """

from collections import Counter
from aocd import get_data
from dotenv import load_dotenv
from typing import Iterable


from helper import data, prod


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


def day10_1(text):
    """Arrange the joltages in order; count the number of each size difference;
        return the product of 1- and 3-jolt differences."""
    numbers = sorted(data(text=text, parser=int, sep="\n"))
    jolts = [0] + numbers + [max(numbers) + 3]
    diffs = [y - x for x, y in zip(jolts[:-1], jolts[1:])]
    jolt_count = dict(Counter(diffs).items())

    print("Part One:")
    for jolt in jolt_count.keys():
        print(f"\t The input has {jolt_count[jolt]} {jolt}-jolt differences")

    print(f"The number of 1-jolt differences multiplied by the number of 3-jolt differences:"
          f" {jolt_count[1]*jolt_count[3]}\n")
    return jolt_count[1], jolt_count[3]


def day10_2(text):
    """Total number of arrangements the adapters to connect the charging outlet to your device?"""
    numbers = sorted(data(text=text, parser=int, sep="\n"))
    jolts = [0] + numbers + [max(numbers) + 3]
    diffs = [y - x for x, y in zip(jolts[:-1], jolts[1:])]
    indices = [0] + [i + 1 for i, x in enumerate(diffs) if x == 3]

    print("Part Two: When a 3-jolt difference occurs, we split the list in two lists.")

    # When split on 3-jolt differences, the lists has length 1, 2, 3, 4, 5
    mapping = {1: 1, 2: 1}
    for i in [3, 4, 5]:
        mapping[i] = calculate_nr_paths_tree(list_length=i)

    arrangements = []
    len_subseq = []

    for i, index in enumerate(indices[:-1]):
        subseq = jolts[index:indices[i + 1]]
        j = len(subseq)
        len_subseq.append(j)
        arrangements.append(mapping[j])

    nr_distinct_arrangements = prod(arrangements)

    print(f"The unique lengths of the contiguous sets are:"
          f" {sorted(list(set(len_subseq)))}")
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

    # --- Part One ---
    day10_1(text=get_data(day=10, year=2020))

    # --- Part Two ---
    day10_2(text=get_data(day=10, year=2020))
