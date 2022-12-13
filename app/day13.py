from functools import cmp_to_key


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a-b
    elif isinstance(a, int) and isinstance(b, list):
        return compare([a], b)
    elif isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])
    else:
        for x, y in zip(a, b):
            if (c:=compare(x, y)) != 0:
                return c
        return compare(len(a), len(b))


def day13a(lines: list[str]) -> str:
    return str(sum([c+1 for a, b, c in zip(lines[::3], lines[1::3], range(len(lines))) if compare(eval(a), eval(b)) < 0]))


def day13b(lines: list[str]) -> str:
    r = sorted([eval(l) for l in lines if l] + [[[2]], [[6]]], key=cmp_to_key(compare))
    return str((r.index([[2]])+1) * (r.index([[6]])+1))
