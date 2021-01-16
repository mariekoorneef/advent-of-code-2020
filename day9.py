""" Advent of Code day 9 """

from aocd import get_data
from dotenv import load_dotenv

from helper import data


def find_two_numbers(numbers: list, target_number: int):
    """ Find two numbers from a list that add up to a specific number """
    for i, number in enumerate(numbers[:-1]):
        complementary = target_number - number
        if complementary in numbers[i + 1:]:
            # print(f"Solution Found: {number} and {complementary}")
            return number, complementary

    print(f"Part One: No solutions exist for target: {target_number}")
    return None


def day9_1(text: str, p: int = 25) -> int:
    """Find the first number in the list of numbers (after a preamble of p=25 numbers)
        which is not the sum of two of the p numbers before it."""
    numbers = data(text=text, parser=int, sep="\n")
    for i in range(0, len(numbers)-p):
        sublist = numbers[i:i+p]
        target = numbers[i+p]
        result = find_two_numbers(numbers=sublist, target_number=target)
        if not result:
            return target


def day9_2(text: str, target: int) -> int:
    """ Find a contiguous subsequence of nums that sums to target; add their max and min. """
    numbers = data(text=text, parser=int, sep="\n")
    subseq = []
    for i, number in enumerate(numbers):
        subseq.append(number)
        while sum(subseq) > target:
            subseq = subseq[1:]
        if sum(subseq) == target and len(subseq) > 1:
            break

    return min(subseq) + max(subseq)


if __name__ == "__main__":
    load_dotenv()

    # --- Part One ---
    invalid_number = day9_1(text=get_data(day=9, year=2020), p=25)

    # --- Part Two ---
    # print(f"Target value: {invalid_number}")

    encryption_weakness = day9_2(text=get_data(day=9, year=2020), target=invalid_number)
    print(f"Part Two: The encryption weakness in my XMAS-encrypted list of numbers: {encryption_weakness}")


