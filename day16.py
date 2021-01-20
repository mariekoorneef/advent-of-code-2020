""" Advent of Code day 16 """

import re
from typing import Tuple, List, Dict, Set
from collections import namedtuple
from itertools import chain
from dotenv import load_dotenv
from aocd.models import Puzzle


from helper import data, prod


TicketInformation = namedtuple("TicketInformation", "rules, your_ticket, nearby_tickets")


def parse_rule(text: str) -> tuple:
    """Given 'class: 1-3 or 5-7' return ('class', (1, 3), (5, 7))"""
    name, r = re.findall(r'[^:(.*)]+', text)
    r11, r12, r21, r22 = map(int, re.findall(r'\d+', r))
    return name, r11, r12, r21, r22


def parse_ticket(text: str) -> Tuple[int]:
    """Given '3,9,18' return (3, 9, 18)"""
    return tuple(map(int, text.split(",")))


def create_set_values(l: list) -> Set[int]:
    """Create a set of possible values for fields"""
    setlist = [set(chain(range(i[1], i[2]+1), range(i[3], i[4]+1))) for i in l]
    return set.union(*setlist)


def create_ticket_validator(l: list) -> dict:
    """Create ticket validator according to the rules l given"""
    def create_lambda(i):
        return lambda x: i[1] <= int(x) <= i[2] or i[3] <= int(x) <= i[4]

    return {rule[0]: create_lambda(rule) for rule in l}


def parse_ticket_information(rules: str, your_ticket, nearby_tickets) -> TicketInformation:
    return TicketInformation(rules=data(text=rules, parser=parse_rule, sep="\n"),
                             your_ticket=parse_ticket(your_ticket.splitlines()[1]),
                             nearby_tickets=data(text=nearby_tickets.replace("nearby tickets:\n", ""), parser=parse_ticket, sep="\n")
                             )


def day16_1(text):
    """Consider the validity of the nearby tickets. """
    ticket_information = parse_ticket_information(*text.split("\n\n"))

    value_validator = create_set_values(l=ticket_information.rules)

    # values that are not valid for any field
    invalid = []
    for ticket in ticket_information.nearby_tickets:
        invalid.append(sum([t for t in ticket if t not in value_validator]))

    print(f"Part One: Consider the validity of the nearby tickets you scanned. "
          f"The ticket scanning error rate is {sum(invalid)}")

    return sum(invalid)


def determine_order_fields(tickets: List[tuple], validator: dict) -> Dict[int, str]:
    """Using the valid ranges for each ticket field, determine what order the fields appear on the tickets.
    Return a mapping of {field_number: field_name} (index into ticket)"""
    order = {i: list(validator.keys()) for i in range(0, len(validator))}

    for ticket in tickets:
        for i, val in enumerate(ticket):
            for key in order[i]:
                if not validator[key](val):
                    order[i].remove(key)

    while any(len(order[i]) > 1 for i in order):
        subdict = {key: value[0] for key, value in order.items() if len(value) == 1}
        subset = set(subdict.values())
        for k in set(order) - set(subdict):
            order[k] = list(set(order[k]) - subset)

    return {k: v[0] for k, v in order.items()}


def day16_2(text):
    """Consider valid nearby tickets. Multiply the six values of the fields that start with 'departure'"""
    ticket_information = parse_ticket_information(*text.split("\n\n"))

    field_validator = create_ticket_validator(ticket_information.rules)

    # keep valid tickets according to day16_1
    value_validator = create_set_values(l=ticket_information.rules)
    nearby_tickets = [ticket for ticket in ticket_information.nearby_tickets if all(t in value_validator for t in ticket)]

    order = determine_order_fields(tickets=nearby_tickets, validator=field_validator)

    # Index of the six fields that start with the word departure.
    departure_ind = [k for k, v in order.items() if v.startswith('departure')]

    answer = prod([ticket_information.your_ticket[ind] for ind in departure_ind])

    print(f"Part Two: Multiply the six values of the fields that start with 'departure': {answer}")


if __name__ == "__main__":
    load_dotenv()

    puzzle = Puzzle(year=2020, day=16)
    input_data = puzzle.input_data
    day16_1(text=input_data)
    day16_2(text=input_data)
