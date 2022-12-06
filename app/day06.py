import re


def day06(s: str, n: int):
    # Constructs and uses a "(.)(?!\1)(.)(?!\1|\2)(.)"... regex
    print(re.search("(.)"+ "".join(["(?!\\" + "|\\".join([str(j + 1) for j in range(i+1)]) + ")(.)" for i in range(n-1)]),s,).end())


def day06a(lines: list[str]):
    day06(lines[0], 4)


def day06b(lines: list[str]):
    day06(lines[0], 14)
