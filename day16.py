import re
from typing import Tuple, List, Dict
from dotenv import load_dotenv
from aocd.models import Puzzle


def parse_rule(text: str) -> tuple:
    """Given 'class: 1-3 or 5-7' return ('class', (1, 3), (5, 7))"""
    name, r = re.findall(r'[^:(.*)]+', text)
    r11, r12, r21, r22 = map(int, re.findall(r'\d+', r))
    return name, r11, r12, r21, r22


def parse_ticket(text: str) -> Tuple[int, ...]:
    """Given '3,9,18' return (3, 9, 18)"""
    return tuple(map(int, text.split(",")))


def create_ticket_validator(l: list) -> dict:
    """Create ticket validator according to the rules l given"""
    def create_lambda(i):
        return lambda x: i[1] <= int(x) <= i[2] or i[3] <= int(x) <= i[4]

    return {rule[0]: create_lambda(rule) for rule in l}


def day16_1(data):
    """Consider the validity of the nearby tickets. """
    rules = [parse_rule(r) for r in data[0].splitlines()]

    field_validator = create_ticket_validator(rules)

    nearby_tickets = [parse_ticket(t) for t in data[2].splitlines()[1:]]
    # values that are not valid for any field
    invalid = []
    invalid_tickets = []
    for ticket in nearby_tickets:
        for t in ticket:
            valid = [bool(field_validator[k](t)) for k in field_validator.keys()]
            if sum(valid) == 0:
                invalid.append(t)
                # for part 2
                invalid_tickets.append(ticket)

    print(f"Part One: Consider the validity of the nearby tickets you scanned. "
          f"The ticket scanning error rate is {sum(invalid)}")

    return sum(invalid), invalid_tickets


def determine_order_fields(tickets: List[tuple], validator: dict) -> Dict[int, str]:
    """Using the valid ranges for each ticket field, determine what order the fields appear on the tickets. """
    order = {i: list(validator.keys()) for i in range(0, len(validator))}

    for ticket in tickets:
        for i, val in enumerate(ticket):
            for key in order[i]:
                if not validator[key](val):
                    order[i].remove(key)

    while not all(len(v) == 1 for k, v in order.items()):
        subdict = {key: value[0] for key, value in order.items() if len(value) == 1}
        subset = set(subdict.values())
        for k1 in set(order) - set(subdict):
            order[k1] = list(set(order[k1]) - subset)

    return {k: v[0] for k, v in order.items()}


def day16_2(data, invalid_tickets):
    """Consider valid nearby tickets. Multiply the six values of the fields that start with 'departure'"""
    rules = [parse_rule(r) for r in data[0].splitlines()]

    field_validator = create_ticket_validator(rules)

    nearby_tickets = [parse_ticket(t) for t in data[2].splitlines()[1:]]
    # discard invalid tickets
    nearby_tickets = [t for t in nearby_tickets if t not in invalid_tickets]

    order = determine_order_fields(tickets=nearby_tickets, validator=field_validator)

    # Index of the six fields that start with the word departure.
    departure_ind = [k for k, v in order.items() if v.startswith('departure')]

    answer = 1
    your_ticket = parse_ticket(data[1].splitlines()[1])
    for ind in departure_ind:
        answer *= your_ticket[ind]

    print(f"Part Two: Multiply the six values of the fields that start with 'departure': {answer}")


if __name__ == "__main__":
    load_dotenv()

    puzzle = Puzzle(year=2020, day=16)
    input_data = puzzle.input_data.split("\n\n")
    error_rate, invalid = day16_1(data=input_data)
    day16_2(data=input_data, invalid_tickets=invalid)
