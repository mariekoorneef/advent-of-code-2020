""" Advent of Code day 13 """

from dotenv import load_dotenv
from aocd.models import Puzzle
from math import sqrt
from itertools import count, islice


def is_prime(n:int) -> bool:
    """Check if number n is a prime number"""
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))


def day13_1(data):
    earliest_timestamp = int(data[0])

    bus_ids = [int(i) for i in data[1].split(",") if i != "x"]

    x1 = [earliest_timestamp // i for i in bus_ids]
    x2 = [(i+1)*j for i, j in zip(x1, bus_ids)]

    # From list of integers get number closest to a given value
    departure_timestamp = min(x2, key=lambda x: abs(x - earliest_timestamp))
    waiting_time = departure_timestamp - earliest_timestamp
    ind = x2.index(departure_timestamp)
    bus_id = bus_ids[ind]
    multiplication = bus_id * waiting_time
    print(f"Part 1: Bus ID of earliest bus: {bus_id}\n"
          f"Waiting time in minutes: {waiting_time}\n"
          f"Multiplication: {multiplication}")

    return multiplication


def day13_2(data):
    buses = [(int(i), ind) for ind, i in enumerate(data.split(",")) if i != "x"]

    buses.sort(key=lambda tup: tup[0], reverse=True)

    bus, time = buses[0]
    step_size = bus
    t = bus - time

    for index, b in enumerate(buses[1:]):
        while (t + b[1]) % b[0] != 0:
            # print(f"increase step {step_size}")
            t += step_size
            # print(t)

        if index == len(buses) - 2:
            print(f"Part 2: the earliest timestamp is: {t}")
            break
        else:
            # uses the observation that bus ids are prime numbers
            step_size *= b[0]
            # print(f"increase step size to {step_size}")

    return t


if __name__ == "__main__":
    load_dotenv()

    puzzle = Puzzle(year=2020, day=13)
    input_data = puzzle.input_data.splitlines()

    day13_1(data=input_data)

    # note bus_ids are prime
    for i in [int(i) for i in input_data[1].split(",") if i != "x"]:
        print(f"Bus ID {i} is prime: {is_prime(n=i)}")

    day13_2(data=input_data[1])
