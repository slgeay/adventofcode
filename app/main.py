import click
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
def day(d: str, i: str) -> None:
    """Launch the puzzle of day D part I

    ex: app day 02 b"""
    func = getattr(globals()[f"day{d}"], f"day{d}{i}")
    with open(f"sample/day{d}.txt") as f, open(f"sample_results/day{d}{i}.txt") as r:
        print("--- Sample ---")
        res = func(f.read().splitlines())
        print(res)
        print("=> " + ("OK" if res == r.read() else "ERROR"))
    with open(f"data/day{d}.txt") as f:
        print("--- Data ---")
        print(func(f.read().splitlines()))


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
