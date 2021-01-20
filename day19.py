""" Advent of Code day 19 """

from helper import data, lines
from dotenv import load_dotenv
from aocd.models import Puzzle
from typing import Optional, List, Tuple


def has_number(text: str) -> bool:
    """Given '4 1 5' return True"""
    return any(char.isdigit() for char in text)


def parse_rules(text: str) -> Tuple[int, list]:
    """ Given '0: 4 1 5' return (0, [4, 1, 5])
        Given '1: 2 3 | 3 2' return (1, [([2, 3], [3, 2])]) """
    k, v = text.replace('"', '').split(": ")
    if "|" in v:
        v = [tuple(list(map(int, i.split(" "))) for i in v.split(" | "))]
    elif has_number(v):
        v = list(map(int, v.split(" ")))
    else:
        v = [v]
    return int(k), v


def match(pat: list, msg: str, rules: dict) -> Optional[str]:
    """ Given pat [4, 1, 5] msg 'ababbb'    return ['a', 1, 5]  ababbb
                                            return [1, 5]       babbb
                                    ...     return []           '' """
    # Failed to match whole pat
    if pat and not msg:
        return None
    # Whole pattern is matched, msg is either '' or still contains character(s)
    elif not pat:
        return msg
    # Match first character, continue
    elif pat[0] == msg[0]:
        return match(pat[1:], msg[1:], rules)
    # Update pattern with the rule
    elif isinstance(pat[0], int):
        update_pat = rules[pat[0]] + pat[1:]
        return match(pat=update_pat, msg=msg, rules=rules)
    # Check each sub-rule
    elif isinstance(pat[0], tuple):
        for tup in pat[0]:
            m = match(tup + pat[1:], msg, rules)
            if m is not None:
                return m
    return None


def nr_matches(rules: dict, received: List[str]) -> int:
    """Return the number of matches that match rule 0"""
    result = [(message, match(pat=rules[0], msg=message, rules=rules)) for message in received]
    return sum([r[1] == '' for r in result])


def day19_1(text):
    rules, received = data(text, parser=lines, sep="\n\n")
    rules = dict(map(parse_rules, rules))

    nr_match = nr_matches(rules=rules, received=received)
    print(f"Part One: {nr_match} messages completely match rule 0")
    return nr_match


def day19_2(text):
    rules, received = data(text, parser=lines, sep="\n\n")
    rules = dict(map(parse_rules, rules))
    d = dict(map(parse_rules, ['8: 42 | 42 8', '11: 42 31 | 42 11 31']))
    rules = {**rules, **d}
    nr_match = nr_matches(rules=rules, received=received)
    print(f"Part Two: {nr_match} messages completely match rule 0")
    return nr_matches


if __name__ == "__main__":
    load_dotenv()

    puzzle = Puzzle(year=2020, day=19)
    day19_1(text=puzzle.input_data)
    day19_2(text=puzzle.input_data)





