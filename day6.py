""" Advent of Code day 6 """

from aocd import get_data
from dotenv import load_dotenv


def day6_1(answers):
    counts = []
    for answer in answers:
        yes = set(answer.replace('\n', ' ').replace('', ' ').split())
        counts.append(len(yes))
    return sum(counts)


def day6_2(answers):
    counts = []
    for answer in answers:
        answer1 = answer.replace('\n', ' ').split()
        setlist = [set(a) for a in answer1]
        u = set.intersection(*setlist)
        counts.append(len(u))
    return sum(counts)


if __name__ == "__main__":
    load_dotenv()

    data = get_data(day=6, year=2020).split("\n\n")

    print(f"Part One: For each group, the number of questions to which anyone answered 'yes': {day6_1(answers=data)}")

    print(f"Part Two: For each group, the number of questions to which everyone answered 'yes': {day6_2(answers=data)}")
