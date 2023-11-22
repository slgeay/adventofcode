def day21a_compute(d: dict, s: str) -> int:
    if d.get(s) and not isinstance(d[s], str):
        return d[s]

    return eval(f"{day21a_compute(d, d[s][:4])} {d[s][5]} {day21a_compute(d, d[s][-4:])}")


def day21a(lines: list[str]) -> str:
    return str(int(day21a_compute({l[:4]: int(l[6:]) if day21b_isnum(l[6]) else l[6:] for l in lines}, "root")))


def day21b_isnum(s: str):
    try:
        float(s)
        return True
    except:
        return False


def day21b_reduce(d: dict, s: str):
    if s == "humn":
        return s

    if not (isinstance(d[s], str)):
        return d[s]

    words = d[s].split()
    for i, w in enumerate(words):
        if day21b_isnum(w) or len(w) != 4 or w == "humn":
            continue
        words[i] = str(day21b_reduce(d, w))
    e = " ".join(words)

    d[s] = "( " + e + " )" if "humn" in e else eval(e)
    return d[s]


def day21b_solve(a: str, b: str) -> str:
    if day21b_isnum(b):
        b = float(b)
    elif day21b_isnum(a):
        a, b = b, float(a)
    else:
        assert False, (a, b)

    while a != "humn":
        assert a[0] == "(" and a[-1] == ")", a
        a = a[2:-2]
        if a[0].isdecimal():
            i = a.index(" ") + 1
            n, op, a = float(a[: i - 1]), a[i], a[i + 2 :]
            if op == "*":
                b = b / n
            elif op == "/":
                b = n / b
            elif op == "+":
                b = b - n
            elif op == "-":
                b = n - b
            else:
                assert False, op
        elif a[-1].isdecimal():
            i = a.rindex(" ") - 1
            a, op, n = a[: i - 1], a[i], float(a[i + 2 :])
            if op == "*":
                b = b / n
            elif op == "/":
                b = b * n
            elif op == "+":
                b = b - n
            elif op == "-":
                b = b + n
            else:
                assert False, op
        else:
            assert False, a

    return str(int(b))


def day21b(lines: list[str]) -> str:
    d = {l[:4]: int(l[6:]) if day21b_isnum(l[6]) else l[6:] for l in lines}
    return day21b_solve(day21b_reduce(d, d["root"][:4]), day21b_reduce(d, d["root"][-4:]))
