import aocd
from aocd.models import Puzzle
import click
import os
import re
import time

from . import *


@click.group()
def main():
    pass


@main.command()
def hello() -> None:
    """Show a little welcome message!"""
    print("Hello ! :wave:")


def format_time(t: int) -> None:
    """ Format the time in a human readable format"""
    if t < (nd:=10**3):
        return f"{t}ns"
    s = f"{t%10**3}ns"
    if t < (nd:=10**3*(d:=nd)):
        return f"{t//d}µs {s}"
    s = f"{t//d%10**3}µs"
    if t < (nd:=10**3*(d:=nd)):
        return f"{t//d}ms {s}"
    s = f"{t//d%10**3}ms"
    if t < (nd:=60*(d:=nd)):
        return f"{t//d%60}s {s}"
    s = f"{t//d%60}s"
    if t < (nd:=60*(d:=nd)):
        return f"{t//d%60}min {s}"
    s = f"{t//d%60}min"
    if t < (nd:=24*(d:=nd)):
        return f"{t//d%24}h {s}"
    return f"{t//nd}j {t//d%24}h {s}"


def print_time(t: int, res: str) -> None:
    """ Print the time in a human readable format and the result"""
    print(format_time(t, res), "=>", res)


@main.command()
@click.argument("d")
@click.argument("i")
@click.option("-s", "--submit", is_flag=True, default=False, help="Submit your answer")
@click.option("-f", "--force", is_flag=True, default=False, help="Try the data even if the sample failed")
def day(d: str, i: str, submit: bool, force: bool) -> None:
    """Launch the puzzle of day D part I

    ex: app day 02 b"""
    func = getattr(globals()[f"day{d}"], f"day{d}{i}")
    with open(f"sample/day{d}.txt") as f, open(f"sample_results/day{d}{i}.txt") as r:
        print("--- Sample ---")
        lines = f.read().splitlines()
        t = time.monotonic_ns()
        res = func(lines)
        t = time.monotonic_ns() - t
        print_time(t, res)
        print("=> " + ("OK" if (t:=(res == r.read())) else "ERROR"))
    if not t and not force:
        return
    with open(f"data/day{d}.txt") as f:
        print("--- Data ---")
        lines = f.read().splitlines()
        t = time.monotonic_ns()
        res = func(lines)
        t = time.monotonic_ns() - t
        print_time(t, res)
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
@click.argument("d", default="-1")
def init(d: str) -> None:
    """Create the files for day D

    ex: app init 02"""
    if d == "-1":
        d = str(aocd.get.current_day())

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
        f.write("\n\n".join([f"def day{d}{i}(lines: list[str]) -> str:\n    return day{d}(lines)\n" for i in ["a", "b"]]))
        f.write(f"\n\ndef day{d}(lines: list[str]) -> str:\n    return str()\n")

    print("Done")


@main.command()
@click.argument("file", default="times")
@click.argument("rounds", default=1)
def times(file: str, rounds: int) -> None:
    """ Time each puzzle"""
    with open(f"{file}.txt", "w") as o:
        for g in sorted(globals().keys()):
            if re.match(r"day\d\d", g):
                for i in ["a", "b"]:
                    if (func := getattr(globals()[g], f"{g}{i}", None)):
                        for d in ["sample", "data"]:
                            with open(f"{d}/{g}.txt") as f:
                                lines = f.read().splitlines()
                                t = time.monotonic_ns()
                                for _ in range(rounds):
                                    func(lines[:])
                                t = (time.monotonic_ns() - t) // rounds
                                print(s:=f"{g},{i},{d},{t},{format_time(t)}")
                                o.write(f"{s}\n")