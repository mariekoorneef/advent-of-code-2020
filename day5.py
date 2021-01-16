""" Advent of Code day 5 """

from aocd import get_data
from dotenv import load_dotenv

from helper import data


def binary_space_partitioning(l: list, seat: str, lower_half_identifier: str, upper_half_identifier: str) -> int:
    """Given the first seven characters of FBFBBFFRLR and 128 rows return 44"""
    for i in seat:
        n = len(l)
        id = int(n/2)
        if i == lower_half_identifier:
            l = l[:id]
        elif i == upper_half_identifier:
            l = l[id:]
        else:
            print(f"{i} does not equal {lower_half_identifier} or {upper_half_identifier}")
    return l[0]


def missing_elements(l: list) -> list:
    """Find missing elements in a list"""
    start, end = l[0], l[-1]
    return sorted(set(range(start, end + 1)).difference(l))


def decode_seat(seat: str) -> int:
    """Decoding FBFBBFFRLR reveals row 44, column 5;
    return seat ID: multiply the row by 8, then add the column."""
    row = binary_space_partitioning(l=list(range(0, 128)),
                                    seat=seat[:7],
                                    lower_half_identifier="F",
                                    upper_half_identifier="B")
    column = binary_space_partitioning(l=list(range(0, 8)),
                                       seat=seat[-3:],
                                       lower_half_identifier="L",
                                       upper_half_identifier="R")

    seat_id = row * 8 + column
    # print(f"{s}: row {row}, column {column}, seat ID {seat_id}.")
    return seat_id


def day5_1(text):
    """Find the maximum seat id. """
    seat_ids = data(text=text, parser=decode_seat, sep="\n")
    return max(seat_ids)


def day5_2(text):
    """Find the missing seat id"""
    seat_ids = data(text=text, parser=decode_seat, sep="\n")
    return missing_elements(l=sorted(seat_ids))[0]


if __name__ == '__main__':
    load_dotenv()

    # -- Part One ---
    input_data = get_data(day=5, year=2020)

    print(f"Part One: The highest seat ID on a boarding pass: {day5_1(text=input_data)}")

    print(f"Part Two: The ID of my seat: {day5_2(text=input_data)}")
