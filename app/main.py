import aocd
from aocd.models import Puzzle
import click
import os
import re

from . import *


@click.group()
def main():
    pass


@main.command()
def hello() -> None:
    """Show a little welcome message!"""
    print("Hello ! :wave:")


@main.command()
@click.argument("d")
@click.argument("i")
@click.option("-s", "--submit", is_flag=True, default=False, help="Submit your answer")
def day(d: str, i: str, submit: bool) -> None:
    """Launch the puzzle of day D part I

    ex: app day 02 b"""
    func = getattr(globals()[f"day{d}"], f"day{d}{i}")
    with open(f"sample/day{d}.txt") as f, open(f"sample_results/day{d}{i}.txt") as r:
        print("--- Sample ---")
        print(res := func(f.read().splitlines()))
        print("=> " + ("OK" if (t:=(res == r.read())) else "ERROR"))
    if not t:
        return
    with open(f"data/day{d}.txt") as f:
        print("--- Data ---")
        print(res := func(f.read().splitlines()))
        if submit:
            aocd.submit(res, day=int(d), year=2022, part=i)


@main.command()
def test() -> None:
    """Test each puzzle with its sample"""
    for g in sorted(globals().keys()):
        if re.match(r"day\d\d", g):
            for i in ["a", "b"]:
                func = getattr(globals()[g], f"{g}{i}")
                with open(f"sample/{g}.txt") as f, open(f"sample_results/{g}{i}.txt") as r:
                    res = func(f.read().splitlines())
                    print(f"{g}{i} => " + ("OK" if res == r.read() else "ERROR"))


@main.command()
@click.argument("d")
def init(d: str) -> None:
    """Create the files for day D

    ex: app init 02"""
    if os.path.exists(f"app/day{d}.py"):
        print(f"Day {d} already exists")
        return

    try:
        aocd.get_data(day=int(d), year=2022)
    except aocd.exceptions.PuzzleLockedError as e:
        print("Puzzle locked: " + str(e))
        return

    puzzle = Puzzle(year=2022, day=int(d))
    print(f"Day {d}: {puzzle.title}")
    print("    "+str(puzzle.easter_eggs))

    with open(f"sample/day{d}.txt", "w") as f:
        f.write(puzzle.example_data+"\n")

    with open(f"data/day{d}.txt", "w") as f:
        f.write(puzzle.input_data+"\n")

    for i in ["a", "b"]:
        with open("sample_results/day{d}{i}.txt".format(d=d, i=i), "w") as f:
            pass

    with open(f"app/day{d}.py", "w") as f:
        f.write("\n\n".join([f"def day{d}{i}(lines: list[str]) -> str:\n    return str()\n" for i in ["a", "b"]]))

    print("Done")
