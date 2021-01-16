""" Advent of Code day 4 """

import re
from aocd import get_data
from dotenv import load_dotenv

from helper import data


def parse_passport(text: str) -> dict:
    """Given a sequence of key:value pairs return a dictionary """
    d = dict(re.findall(r'([a-z]+):([^\s]+)', text))
    return d


def check_hgt(s: str) -> bool:
    """Check height: a number followed by either cm or in """
    if re.match(r"^[0-9]{3}cm$", s):
        # If cm, the number must be at least 150 and at most 193.
        return 150 <= int(s[:-2]) <= 193
    elif re.match(r"^[0-9]{2}in$", s):
        # If in, the number must be at least 59 and at most 76.
        return 59 <= int(s[:-2]) <= 76
    else:
        return False


# byr (Birth Year) - four digits; at least 1920 and at most 2002
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
passport_validator = {
    "byr": lambda v: 1920 <= int(v) <= 2002,
    "iyr": lambda v: 2010 <= int(v) <= 2020,
    "eyr": lambda v: 2020 <= int(v) <= 2030,
    "hgt": lambda v: check_hgt(v),
    "hcl": lambda v: bool(re.match(r"^\#([0-9A-Fa-f]){6}$", v)),
    "ecl": lambda v: v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda v: bool(re.match(r"^\d{9}$", v))
}


def check_passport_contains_keys(passport: dict, keys: set) -> bool:
    return keys.issubset(passport)


def day4_1(text):
    """Count the number of passports that have all required_fields. """
    passports = data(text=text, parser=parse_passport, sep="\n\n")
    keys = set(passport_validator.keys())
    valid = [check_passport_contains_keys(passport, keys) for passport in passports]
    return sum(valid)


def day4_2(text):
    """Count the number of passports that have all required fields and valid values. """
    valid = []
    passports = data(text=text, parser=parse_passport, sep="\n\n")
    keys = set(passport_validator.keys())
    for passport in passports:
        if check_passport_contains_keys(passport, keys):
            valid.append(all(passport_validator[k](v) for k, v in passport.items() if k != "cid"))
    return sum(valid)


if __name__ == "__main__":
    load_dotenv()

    # --- Part One ---
    optional = {"cid"}

    input_data = get_data(day=4, year=2020)

    print(f"Part One: {day4_1(text=input_data)} passports are valid")

    # --- Part Two ---
    print(f"Part Two: {day4_2(text=input_data)} passports are valid")

