""" Advent of Code day 2 """

from aocd import get_data
from dotenv import load_dotenv
import re

from helper import data


def parse_password_policy(line: str) -> tuple:
    """Given '1-3 a: abcde' return (1, 3, a, abcde)"""
    a, b, letter, password = re.findall(r'[^-:\s]+', line)
    return int(a), int(b), letter, password


def day2_1(text):
    """Does policies password have between a and b occurrences of letter?"""
    policies = data(text=text, parser=parse_password_policy, sep="\n")
    valid = []
    for policy in policies:
        a, b, letter, password = policy
        count = password.count(letter)
        valid.append(a <= count <= b)
    return sum(valid)


def day2_2(text):
    """Does exactly one of the positions a or b in the policy password contain letter"""
    policies = data(text=text, parser=parse_password_policy, sep="\n")
    valid = []
    for policy in policies:
        a, b, letter, password = policy
        positions = {pos + 1 for pos, char in enumerate(password) if char == letter}
        valid.append(len({a, b} & positions))
    return valid.count(1)


if __name__ == "__main__":
    load_dotenv()

    input_data = get_data(day=2, year=2020)

    # -- Part One ---

    valid_passwords_1 = day2_1(text=input_data)
    print(f"Part One: {valid_passwords_1} passwords are valid according to their policies")

    # -- Part Two ---
    valid_passwords_2 = day2_2(text=input_data)

    print(f"Part Two: {valid_passwords_2} passwords are valid according to their policies")
