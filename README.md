# advent-of-code-2020

** WORK IN PROGRESS **

See [Advent of Code 2020](https://adventofcode.com/2020) for the problem descriptions.

### Run
- [`advent-of-code-data`](https://pypi.org/project/advent-of-code-data/) python package
- Follow the instructions to find `AOC_SESSION` variable

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
Use `pytest` to test the examples given in the problem descriptions.
```sh
# in the virtualenv 
pip install pytest

# run
pytest
```