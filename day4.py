""" Advent of Code day 4 """

import re
from aocd import get_data
from dotenv import load_dotenv

from helper import data


def parse_passport(text: str) -> dict:
    """Given a sequence of key:value pairs return a dictionary """
    d = dict(re.findall(r'([a-z]+):([^\s]+)', text))
    return d


def check_interval(s: str, lower: int, upper: int) -> bool:
    """Check if parsed string is in the interval"""
    return lower <= int(s) <= upper


def check_hgt(s: str) -> bool:
    """Check height: a number followed by either cm or in"""
    if re.match(r"^[0-9]{3}cm$", s):
        # If cm, the number must be at least 150 and at most 193.
        return check_interval(s[:-2], 150, 193)
    elif re.match(r"^[0-9]{2}in$", s):
        # If in, the number must be at least 59 and at most 76.
        return check_interval(s[:-2], 59, 76)
    else:
        return False


def check_passport_field_values(passport: dict) -> bool:
    """Check if rules apply to passport fields"""
    # byr (Birth Year) - four digits; at least 1920 and at most 2002
    byr = check_interval(passport["byr"], 1920, 2002)
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    iyr = check_interval(passport["iyr"], 2010, 2020)
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    eyr = check_interval(passport["eyr"], 2020, 2030)
    # hgt
    hgt = check_hgt(passport["hgt"])
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    hcl = bool(re.match(r"^\#([0-9A-Fa-f]){6}$", passport["hcl"]))
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    ecl = passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    pid = bool(re.match(r"^\d{9}$", passport["pid"]))

    return [byr, iyr, eyr, hgt, hcl, ecl, pid] == [True] * 7


def check_passport_contains_fields(passport: dict, required_fields: set) -> bool:
    return required_fields.issubset(passport)


def day4_1(text, required_fields=None):
    """Count the number of passports that have all required_fields. """
    if required_fields is None:
        required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    passports = data(text=text, parser=parse_passport, sep="\n\n")
    valid = [check_passport_contains_fields(passport, required_fields) for passport in passports]
    return sum(valid)


def day4_2(text, required_fields=None):
    """Count the number of passports that have all required fields and valid values. """
    if required_fields is None:
        required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    valid = []
    passports = data(text=text, parser=parse_passport, sep="\n\n")
    for passport in passports:
        if check_passport_contains_fields(passport, required_fields):
            valid.append(check_passport_field_values(passport))
        else:
            valid.append(False)
    return sum(valid)


if __name__ == "__main__":
    load_dotenv()

    # --- Part One ---
    optional = {"cid"}

    input_data = get_data(day=4, year=2020)

    print(f"Part One: {day4_1(text=input_data)} passports are valid")

    # --- Part Two ---
    print(f"Part Two: {day4_2(text=input_data)} passports are valid")

