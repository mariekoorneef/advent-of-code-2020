# advent-of-code-2020

My sample solutions for [Advent of Code 2020](https://adventofcode.com/2020), up to day 20 - part 1.

### Run locally
To get my puzzle input I have used Python package [`advent-of-code-data`](https://pypi.org/project/advent-of-code-data/). It requires your `AOC_SESSION`, see instructions.

```sh
# create a virtualenv
virtualenv .virtualenv

# activate environment
. .virtualenv/bin/activate

# install packages
pip install -r requirements.txt

# Set AOC_SESSION environment variable in .env-file 
AOC_SESSION=my_aoc_session > .env

# Run a day
python day18.py
```

### Tests
I have used `pytest` to test the examples given in the problem descriptions.
```sh
# in the virtualenv 
pip install pytest

# run
pytest
```