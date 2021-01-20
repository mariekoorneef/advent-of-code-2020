""" Advent of Code day 20 """

from typing import List, Tuple
from helper import data, prod
from dotenv import load_dotenv
from aocd.models import Puzzle


def parse_tile(text: str) -> Tuple[int, List[List[str]]]:
    """ Given 'Tile 1567:\n.####.##.#\n.......#..\n.###..###.\n.....#..#.\n..#....#..\n#......###\n#..#.....#\n#....##...\n...###...#\n#.#.#..##.'
        return (1567, [['.', '#', '#', '#', '#', '.', '#', '#', '.', '#'], ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'], ...] """
    id_tile, image = text.split(":\n")
    return int(id_tile.replace("Tile ", "")), [list(i) for i in image.split("\n")]


def transpose_list_of_lists(l: List[List[str]]) -> List[List[str]]:
    """Given: [[1, 2, 3], [4, 5, 6]] return [[1, 4], [2, 5], [3, 6]]"""
    return list(map(list, zip(*l)))


def rotate_and_flip(tile: List[List[str]]) -> List[str]:
    """Given a tile, return all borders when rotated and flipped """
    trans = transpose_list_of_lists(tile)
    return [
        "".join(tile[0]),
        # reverse/ mirroring
        "".join(tile[0][::-1]),
        "".join(tile[-1]),
        "".join(tile[-1])[::-1],
        "".join(trans[0]),
        "".join(trans[0])[::-1],
        "".join(trans[-1]),
        "".join(trans[-1])[::-1]
    ]


def day20_1(text):
    input_data = data(text=text, parser=parse_tile, sep="\n\n")

    borders = dict()

    for nr, tile in input_data:
        borders[nr] = rotate_and_flip(tile)

    # For each tile, return a list of IDs of adjacent tiles.
    adjacent_tiles = dict()

    for tile, value in borders.items():
        other = {k: borders[k] for k in borders if k != tile}
        adjacent_tiles[tile] = [k for k, v in other.items() if not set(value).isdisjoint(v)]

    # Corner tiles have two borders, i.e. two adjacent tiles
    corner_tiles = [k for k, v in adjacent_tiles.items() if len(v) == 2]
    print(f"Part One: multiply the id's of the four corner tiles: {prod(corner_tiles)}")

    return prod(corner_tiles)


if __name__ == "__main__":
    load_dotenv()

    puzzle = Puzzle(year=2020, day=20)
    day20_1(text=puzzle.input_data)
