""" Advent of Code day 7 """

import re
from aocd import get_data
from dotenv import load_dotenv


def create_children(nodes: dict, l: list) -> list:
    """Create a tree structure from a set of parent-child relationships in nodes"""
    d = []
    while l:
        for i in l:
            count, color = i
            children = nodes[color]
            d.append({"id": color, "count": int(count), "children": create_children(nodes=nodes, l=children)})
        return d


def count_bags(dic: dict, count: int = 0):
    """Given a tree structure dic, parse through the tree to count the number of individual bags"""
    if not dic["children"]:
        return count
    factor = dic["count"]
    return count + factor * sum(count_bags(key, key["count"]) for key in dic["children"])


def parse_rule(rule: str) -> tuple:
    """Given 'light red bags contain 1 bright white bag, 2 muted yellow bags' return
    (light red, [('1', 'bright white'), ('2', 'muted yellow')])"""
    key = rule[:rule.find(" bags contain")]
    colors = re.findall(r'\d+ (.*?) bag', rule)
    quantity = re.findall(r'\d+', rule)
    value = list(zip(quantity, colors))
    return key, value


def day7_1(rules, x):
    colors = []
    while x:
        s = x
        x = []
        for rule in rules:
            if any(value in rule.split('contain')[1] for value in s):
                colors.append(rule[:rule.find("bags contain")])
                x.append(rule[:rule.find("bags contain")])

    return len(set(colors))


def day7_2(rules):
    # Create a dictionary with parent child relationships
    nodes = {}
    for r in rules:
        parent, children = parse_rule(rule=r)
        # print(f"{parent}: {list(zip(d, children))}")
        if parent in nodes.keys():
            print(f"{parent} already in dictionary")
        nodes[parent] = children
    # print(nodes)

    # Create a tree structure from a set of parent-child relationships starting at 'shiny gold'
    tree = {"id": "shiny gold",
            "count": 1,
            "children": create_children(nodes=nodes, l=nodes["shiny gold"])
            }

    # print(tree)

    return count_bags(tree)


if __name__ == "__main__":
    load_dotenv()

    lines = get_data(day=7, year=2020).splitlines()

    # --- Part One ---
    print(f"Part One: {day7_1(rules=lines, x=['shiny gold'])} bag colors can eventually contain "
          f"at least one shiny gold bag")

    # --- Part Two ---
    print(f"Part Two: {day7_2(rules=lines)} individual bags are required inside my single shiny gold bag")
