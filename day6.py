""" Advent of Code day 6 """

from aocd import get_data
from dotenv import load_dotenv


def day6_1(answers):
    """What is the sum of counts for each group to which anyone answered 'yes'? """
    return sum([len(set(answer.replace('\n', '')))
                for answer in answers])


def day6_2(answers):
    """What is the sum of counts for each group to which everyone answered 'yes'? """
    counts = []
    for answer in answers:
        setlist = [set(a) for a in answer.splitlines()]
        u = set.intersection(*setlist)
        counts.append(len(u))
    return sum(counts)


if __name__ == "__main__":
    load_dotenv()

    input_data = get_data(day=6, year=2020).split("\n\n")

    print(f"Part One: For each group, the number of questions to which anyone answered 'yes': {day6_1(answers=input_data)}")

    print(f"Part Two: For each group, the number of questions to which everyone answered 'yes': {day6_2(answers=input_data)}")
