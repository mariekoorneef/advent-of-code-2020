from day2 import day2_1, day2_2, parse_password_policy
from day3 import day3_1, day3_2
from day4 import day4_1, day4_2, parse_passport
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


def test_day2():
    lines = """1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc""".splitlines()
    password_policies = [parse_password_policy(line) for line in lines]
    assert day2_1(policies=password_policies) == 2
    assert day2_2(policies=password_policies) == 1


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
    example = file.read().split("\n\n")
    pps = [parse_passport(t) for t in example]
    assert day4_1(passports=pps) == 2


def test_day4_2_valid():
    text = ["pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980\nhcl:#623a2f"]
    pps = [parse_passport(t) for t in text]
    assert day4_2(passports=pps) == 1


def test_day4_2_invalid():
    text = ["eyr:1972 cid:100\nhcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926"]
    pps = [parse_passport(t) for t in text]
    assert day4_2(passports=pps) == 0


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
    example = file.read().splitlines()
    assert day7_1(rules=example, x=["shiny gold"]) == 4
    assert day7_2(rules=example) == 32


def test_day8():
    example = "nop +0\n" \
              "acc +1\n" \
              "jmp +4\n" \
              "acc +3\n" \
              "jmp -3\n" \
              "acc -99\n" \
              "acc +1\n" \
              "jmp -4\n" \
              "acc +6".splitlines()

    assert day8_1(data=example) == 5
    assert day8_2(data=example) == 8


def test_day9():
    filename = "test_input/day9_example.txt"
    print(f"The filename: {filename}")
    file = open(filename, "r+")
    example = file.read().splitlines()
    assert day9_1(data=example, length=5) == 127
    assert day9_2(data=example, target=127) == 62


def test_day10():
    example1 = "16\n10\n15\n5\n1\n11\n7\n19\n6\n12\n4".splitlines()
    example2 = "28\n33\n18\n42\n31\n14\n46\n20\n48\n47\n24\n23\n49\n45\n19" \
               "\n38\n39\n11\n1\n32\n25\n35\n8\n17\n7\n9\n4\n2\n34\n10\n3".splitlines()
    assert day10_1(data=example1) == (7, 5)
    assert day10_1(data=example2) == (22, 10)
    assert day10_2(data=example1) == 8
    assert day10_2(data=example2) == 19208


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
                 "L.LLLLL.LL\n".splitlines()
    assert day11_1(data=example) == 37
    assert day11_2(data=example) == 26


def test_day12():
    example = "F10\nN3\nF7\nR90\nF11".splitlines()
    assert day12_1(data=example) == 25
    assert day12_2(data=example) == 286


def test_day13():
    test_input1 = "939\n7,13,x,x,59,x,31,19".splitlines()
    assert day13_1(data=test_input1) == 295
    assert day13_2(data="7,13,x,x,59,x,31,19") == 1068781
    assert day13_2(data="17,x,13,19") == 3417
    assert day13_2(data="67,7,59,61") == 754018
    assert day13_2(data="67,x,7,59,61") == 779210
    assert day13_2(data="67,7,x,59,61") == 1261476
    assert day13_2(data="1789,37,47,1889") == 1202161486


def test_day14():
    example1 = "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X\n" \
               "mem[8] = 11\n" \
               "mem[7] = 101\n" \
               "mem[8] = 0".splitlines()

    example2 = "mask = 000000000000000000000000000000X1001X\n" \
               "mem[42] = 100\n" \
               "mask = 00000000000000000000000000000000X0XX\n" \
               "mem[26] = 1".splitlines()

    assert day14_1(data=example1) == 165
    assert day14_2(data=example2) == 208


def test_day15():
    assert day15(data="0,3,6".split(",")) == 436
    assert day15(data="1,3,2".split(",")) == 1
    assert day15(data="2,1,3".split(",")) == 10
    assert day15(data="1,2,3".split(",")) == 27
    assert day15(data="2,3,1".split(",")) == 78
    assert day15(data="3,2,1".split(",")) == 438
    assert day15(data="3,1,2".split(",")) == 1836
    # assert day15(data="0,3,6".split(","), threshold=30000000) == 175594
