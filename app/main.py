import click
from . import *


@click.group()
def main():
    pass


@main.command()
def hello() -> None:
    """Show a little welcome message!"""
    print("Hello ! :wave:")


@main.command()
@click.argument('d')
@click.argument('i')
def day(d:str, i:str) -> None:
    """Launch the puzzle of day D part I
    
    ex: app day 02 b"""
    with open(f'data/day{d}.txt') as f:
        getattr(globals()[f'day{d}'], f'day{d}{i}')(f.readlines())
