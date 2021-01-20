""" Advent of Code day 18 """

import operator
import pyparsing
from dotenv import load_dotenv
from aocd.models import Puzzle
from typing import List

ops = {"+": operator.add, "*": operator.mul}


def calculate(x: list, func, *args) -> int:
    """Parentheses (represented as lists) can override the evaluation order """
    for ind, expr in enumerate(x):
        if isinstance(expr, list):
            x[ind] = calculate(expr, func)

    return func(x)


def left_to_right(expr: List[str]) -> int:
    """Operators are evaluated left-to-right """
    if len(expr) == 1:
        return int(expr[0])
    else:
        op1, op, op2, *rest = expr
        val = ops[op](int(op1), int(op2))
        return val if not rest else left_to_right([val, *rest])


def addition_before_multiplication(expr: List[str]) -> int:
    """Addition is evaluated before multiplication. """
    if len(expr) == 1:
        return int(expr[0])
    elif "*" in expr:
        ind = expr.index("*")
        return addition_before_multiplication(expr[:ind]) * addition_before_multiplication(expr[ind + 1:])
    else:
        return sum([int(x) for x in expr if x != "+"])


def evaluate_expression(text: str, func, *args) -> int:
    """Evaluate the expression on each line """
    expr = pyparsing.nestedExpr().parseString(f"({text})").asList()
    val = calculate(func=func, x=expr)
    return val


def day18_1(puzzle_input, part="One", func=left_to_right):
    """What is the sum of the evaluated expressions? """
    results = list(map(lambda p: evaluate_expression(p, func), puzzle_input.split("\n")))
    print(f"Part {part}: the sum of the evaluated expressions is: {sum(results)}")
    return sum(results)


def day18_2(puzzle_input): return day18_1(puzzle_input, part="Two", func=addition_before_multiplication)


if __name__ == "__main__":
    load_dotenv()

    puzzle = Puzzle(year=2020, day=18)
    day18_1(puzzle_input=puzzle.input_data)
    day18_2(puzzle_input=puzzle.input_data)
