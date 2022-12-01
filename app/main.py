import click
import day01


@click.group()
def main():
    pass


@main.command()
def hello() -> None:
    """Show a little welcome message!"""
    print("Hello ! :wave:")


@main.command()
def day01a() -> None:
    day01.day01a()

@main.command()
def day01b() -> None:
    day01.day01b()
