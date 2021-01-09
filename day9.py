""" Advent of Code day 9 """

from aocd import get_data
from dotenv import load_dotenv


def find_two_numbers(numbers: list, target_number: int):
    """ Find two numbers from a list that add up to a specific number """
    for i, number in enumerate(numbers[:-1]):
        complementary = target_number - number
        if complementary in numbers[i + 1:]:
            # print(f"Solution Found: {number} and {complementary}")
            return number, complementary

    print(f"Part One: No solutions exist for target: {target_number}")
    return None


def day9_1(data: list, length: int) -> int:
    numbers = [int(i) for i in data]
    for i in range(0, len(numbers)-length):
        sublist = numbers[i:i+length]
        target = numbers[i+length]
        result = find_two_numbers(numbers=sublist, target_number=target)
        if not result:
            return target


def day9_2(data: list, target: int) -> int:
    numbers = [int(i) for i in data]
    s = []
    for i, number in enumerate(numbers):
        s.append(number)
        while sum(s) > target:
            s = s[1:]
        if sum(s) == target and len(s) > 1:
            break

    return min(s) + max(s)


if __name__ == "__main__":
    load_dotenv()

    lines = get_data(day=9, year=2020).splitlines()

    # --- Part One ---
    invalid_number = day9_1(data=lines, length=25)

    # --- Part Two ---
    # print(f"Target value: {invalid_number}")

    encryption_weakness = day9_2(data=lines, target=invalid_number)
    print(f"Part Two: The encryption weakness in my XMAS-encrypted list of numbers: {encryption_weakness}")


