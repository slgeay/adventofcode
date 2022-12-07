import re


def day06(s: str, n: int) -> str:
    # Constructs and uses a "(.)(?!\1)(.)(?!\1|\2)(.)"... regex
    return str(re.search("".join(["(.)(?!\\"+"|\\".join([str(j+1) for j in range(i+1)])+")" for i in range(n-1)])+".",s).end())


def day06_multi(lines: list[str], n: int) -> str:
    # Useful only because of multiple samples
    return "\n".join([day06(l, n) for l in lines])


def day06a(lines: list[str]) -> str:
    return day06_multi(lines, 4)


def day06b(lines: list[str]) -> str:
    return day06_multi(lines, 14)
