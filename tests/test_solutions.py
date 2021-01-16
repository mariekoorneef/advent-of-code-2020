from day2 import day2_1, day2_2
from day3 import day3_1, day3_2
from day4 import day4_1, day4_2
from day5 import decode_seat
from day6 import day6_1, day6_2
from day7 import day7_1, day7_2
from day8 import day8_1, day8_2
from day9 import day9_1, day9_2
from day10 import day10_1, day10_2
from day11 import day11_1, day11_2
from day12 import day12_1, day12_2
from day13 import day13_1, day13_2
from day14 import day14_1, day14_2
from day15 import day15
from day16 import day16_1, parse_rule, parse_ticket, create_ticket_validator, determine_order_fields, Information
from day17 import day17_1, day17_2, parse_state
from day18 import evaluate_expression, left_to_right, addition_before_multiplication

from helper import data


def test_day2():
    example = """1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc"""
    assert day2_1(text=example) == 2
    assert day2_2(text=example) == 1


def test_day3():
    filename = "test_input/day3_example.txt"
    print(f"The filename: {filename}")
    file = open(filename, "r+")
    example = file.read().splitlines()
    picture = [list(line) for line in example]
    assert day3_1(area=picture, right=3, down=1) == 7
    assert day3_2(area=picture) == 336


def test_day4():
    filename = "test_input/day4_example.txt"
    print(f"The filename: {filename}")
    file = open(filename, "r+")
    example = file.read()
    assert day4_1(text=example) == 2


def test_day4_2_valid():
    text = "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980\nhcl:#623a2f"
    assert day4_2(text=text) == 1


def test_day4_2_invalid():
    text = "eyr:1972 cid:100\nhcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926"
    assert day4_2(text=text) == 0


def test_day5():
    seats = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
    answers = [357, 567, 119, 820]
    for s, a in zip(seats, answers):
        assert decode_seat(seat=s) == a


def test_day6():
    example_1 = """abcx\nabcy\nabcz""".split("\n\n")
    example_2 = """abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb""".split("\n\n")
    assert day6_1(answers=example_1) == 6
    assert day6_1(answers=example_2) == 11
    assert day6_2(answers=example_2) == 6


def test_day7():
    filename = "test_input/day7_example1.txt"
    print(f"The filename: {filename}")
    file = open(filename, "r+")
    example = file.read()
    assert day7_1(text=example, target="shiny gold") == 4
    assert day7_2(text=example) == 32


def test_day8():
    example = "nop +0\n" \
              "acc +1\n" \
              "jmp +4\n" \
              "acc +3\n" \
              "jmp -3\n" \
              "acc -99\n" \
              "acc +1\n" \
              "jmp -4\n" \
              "acc +6"

    assert day8_1(text=example) == 5
    assert day8_2(text=example) == 8


def test_day9():
    example = '35\n20\n15\n25\n47\n40\n62\n55\n65\n95\n102\n117\n150\n182\n127\n219\n299\n277\n309\n576'
    assert day9_1(text=example, p=5) == 127
    assert day9_2(text=example, target=127) == 62


def test_day10():
    example1 = "16\n10\n15\n5\n1\n11\n7\n19\n6\n12\n4"
    example2 = "28\n33\n18\n42\n31\n14\n46\n20\n48\n47\n24\n23\n49\n45\n19" \
               "\n38\n39\n11\n1\n32\n25\n35\n8\n17\n7\n9\n4\n2\n34\n10\n3"
    assert day10_1(text=example1) == (7, 5)
    assert day10_1(text=example2) == (22, 10)
    assert day10_2(text=example1) == 8
    assert day10_2(text=example2) == 19208


def test_day11():
    example = "L.LL.LL.LL\n" \
                 "LLLLLLL.LL\n" \
                 "L.L.L..L..\n" \
                 "LLLL.LL.LL\n" \
                 "L.LL.LL.LL\n" \
                 "L.LLLLL.LL\n" \
                 "..L.L.....\n" \
                 "LLLLLLLLLL\n" \
                 "L.LLLLLL.L\n" \
                 "L.LLLLL.LL\n"
    assert day11_1(text=example) == 37
    assert day11_2(text=example) == 26


def test_day12():
    example = "F10\nN3\nF7\nR90\nF11"
    assert day12_1(text=example) == 25
    assert day12_2(text=example) == 286


def test_day13():
    test_input1 = "939\n7,13,x,x,59,x,31,19".splitlines()
    assert day13_1(text=test_input1) == 295
    assert day13_2(text="7,13,x,x,59,x,31,19") == 1068781
    assert day13_2(text="17,x,13,19") == 3417
    assert day13_2(text="67,7,59,61") == 754018
    assert day13_2(text="67,x,7,59,61") == 779210
    assert day13_2(text="67,7,x,59,61") == 1261476
    assert day13_2(text="1789,37,47,1889") == 1202161486


def test_day14():
    example1 = "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X\n" \
               "mem[8] = 11\n" \
               "mem[7] = 101\n" \
               "mem[8] = 0"

    example2 = "mask = 000000000000000000000000000000X1001X\n" \
               "mem[42] = 100\n" \
               "mask = 00000000000000000000000000000000X0XX\n" \
               "mem[26] = 1"

    assert day14_1(text=example1) == 165
    assert day14_2(text=example2) == 208


def test_day15():
    assert day15(text="0,3,6") == 436
    assert day15(text="1,3,2") == 1
    assert day15(text="2,1,3") == 10
    assert day15(text="1,2,3") == 27
    assert day15(text="2,3,1") == 78
    assert day15(text="3,2,1") == 438
    assert day15(text="3,1,2") == 1836
    # assert day15(data="0,3,6", threshold=30000000) == 175594


def test_day16():
    example1 = "class: 1-3 or 5-7\n" \
               "row: 6-11 or 33-44\n" \
               "seat: 13-40 or 45-50\n\n" \
               "your ticket:\n" \
               "7,1,14\n\n" \
               "nearby tickets:\n" \
               "7,3,47\n" \
               "40,4,50\n" \
               "55,2,20\n" \
               "38,6,12"
    example2 = "class: 0-1 or 4-19\n" \
               "row: 0-5 or 8-19\n" \
               "seat: 0-13 or 16-19\n\n" \
               "your ticket:\n" \
               "11,12,13\n\n" \
               "nearby tickets:\n" \
               "3,9,18\n" \
               "15,1,5\n" \
               "5,14,9"
    assert day16_1(text=example1) == 71
    assert parse_rule('class: 1-3 or 5-7') == ('class', 1, 3, 5, 7)
    assert parse_ticket('3,9,18') == (3, 9, 18)

    info = Information(text=example2)
    info.parse_information()
    validator = create_ticket_validator(info.rules)
    assert determine_order_fields(tickets=info.nearby_tickets, validator=validator) == {0: 'row', 1: 'class', 2: 'seat'}


def test_day17():
    example = ".#.\n..#\n###"
    input_data = data(example, parser=parse_state, sep="\n")

    assert day17_1(input_data) == 112
    assert day17_2(input_data) == 848


def test_day18():
    # Part 1
    assert left_to_right(expr="1 + 2 * 3 + 4 * 5 + 6".split()) == 71
    assert evaluate_expression(text="1 + 2 * 3 + 4 * 5 + 6", func=left_to_right) == 71
    assert evaluate_expression(text="1 + (2 * 3) + (4 * (5 + 6))", func=left_to_right) == 51
    assert evaluate_expression(text="2 * 3 + (4 * 5)", func=left_to_right) == 26
    assert evaluate_expression(text="5 + (8 * 3 + 9 + 3 * 4 * 3)", func=left_to_right) == 437
    assert evaluate_expression(text="5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", func=left_to_right) == 12240
    assert evaluate_expression(text="((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", func=left_to_right) == 13632

    # Part 2
    assert addition_before_multiplication(expr="1 + 2 * 3 + 4 * 5 + 6".split()) == 231
    assert evaluate_expression(text="1 + 2 * 3 + 4 * 5 + 6", func=addition_before_multiplication) == 231
    assert evaluate_expression(text="1 + (2 * 3) + (4 * (5 + 6))", func=addition_before_multiplication) == 51
    assert evaluate_expression(text="2 * 3 + (4 * 5)", func=addition_before_multiplication) == 46
    assert evaluate_expression(text="5 + (8 * 3 + 9 + 3 * 4 * 3)", func=addition_before_multiplication) == 1445
    assert evaluate_expression(text="5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", func=addition_before_multiplication) == 669060
    assert evaluate_expression(text="((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", func=addition_before_multiplication) == 23340
