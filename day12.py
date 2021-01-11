""" Advent of Code day 12 """

from dotenv import load_dotenv
from aocd.models import Puzzle


def day12_1(data):
    ship_location = {
        "N": 0,
        "S": 0,
        "E": 0,
        "W": 0
    }

    facing = "E"
    degree = 90
    compass = {0: "N", 90: "E", 180: "S", 270: "W"}

    for instruction in data:
        action = instruction[:1]
        value = int(instruction[1:])
        print(f"Action: {action} with value {value}")
        if action in ("R", "L") and value > 360:
            print(f"WARNING")

        if action == "F":
            # Action F means to move forward by the given value in the direction the ship is currently facing.
            ship_location[facing] += value
        elif action in ("N", "S", "E", "W"):
            # Action N means to move north by the given value. etc.
            ship_location[action] += value
        elif action == "R":
            # Action R means to turn right the given number of degrees.
            degree = (degree + value) % 360
            facing = compass[degree]
        elif action == "L":
            # Action L means to turn left the given number of degrees.
            degree = degree - value
            if degree < 0:
                degree = 360 + degree
            facing = compass[degree]

    print(f"Ship location: {ship_location}")

    manhattan_dist = abs(ship_location["E"]-ship_location["W"]) + abs(ship_location["N"]-ship_location["S"])

    return manhattan_dist


def day12_2(data):
    ship_location = {
        "N": 0,
        "S": 0,
        "E": 0,
        "W": 0
    }
    waypoint_location = {
        "N": 1,
        "E": 10,
    }

    waypoint_dir = ["N", "E"]
    compass = {0: "N", 90: "E", 180: "S", 270: "W"}
    compass_reverse = {"N": 0, "E": 90, "S": 180, "W": 270}

    for instruction in data:
        action = instruction[:1]
        value = int(instruction[1:])
        print(f"Action: {action} with value {value}")
        print(ship_location)
        print(waypoint_location)

        if action == "F":
            # Action F means to move forward to the waypoint a number of times equal to the given value.
            for k, v in waypoint_location.items():
                ship_location[k] += (value * v)
        elif action in waypoint_dir:
            waypoint_location[action] += value
        elif action in {"N", "E", "S", "W"} - set(waypoint_dir):
            # Action N means to move the waypoint north by the given value. etc.
            if action == "N":
                waypoint_location["S"] -= value
            elif action == "E":
                waypoint_location["W"] -= value
            elif action == "S":
                waypoint_location["N"] -= value
            elif action == "W":
                waypoint_location["E"] -= value
        else:
            new_dir = []
            values = []

            if action == "R":
                # Action R means to rotate the waypoint around the ship right (clockwise)
                # the given number of degrees.
                for w in waypoint_dir:
                    deg = (compass_reverse[w] + value) % 360
                    dir = compass[deg]
                    new_dir.append(dir)
                    values.append(waypoint_location[w])
            elif action == "L":
                # Action L means to rotate the waypoint around the ship left (counter-clockwise)
                # the given number of degrees.
                for w in waypoint_dir:
                    deg = compass_reverse[w] - value
                    if deg < 0:
                        deg = 360 + deg
                    dir = compass[deg]
                    new_dir.append(dir)
                    values.append(waypoint_location[w])

            waypoint_location = dict(zip(new_dir, values))

            waypoint_dir = new_dir

    print(ship_location)
    manhattan_dist = abs(ship_location["E"] - ship_location["W"]) + abs(ship_location["N"] - ship_location["S"])
    return manhattan_dist


if __name__ == "__main__":
    load_dotenv()

    puzzle = Puzzle(year=2020, day=12)
    input_data = puzzle.input_data.splitlines()

    # --- Part One ---
    manhattan_distance = day12_1(data=input_data)
    print(f"Part One: Manhattan distance: {manhattan_distance}")

    # --- Part Two ---
    manhattan_distance = day12_2(data=input_data)
    print(f"Part Two: Manhattan distance: {manhattan_distance}")
