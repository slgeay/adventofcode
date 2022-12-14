import copy
import re

print_start = False
print_result = False


def print_map(b: bool, w: dict[int, set[int]], m: dict[int, set[int]], xmin: int, xmax: int, ymax: int):
    if b:
        print("000", "".join(["x" if x == 500 else " " for x in range(xmin, xmax + 1)]))
        for y in range(0, ymax + 1):
            print("{:0>3}".format(y), "".join(["#" if x in sorted(w.get(y) or []) else "o" if x in (m.get(y) or []) else " " for x in range(xmin, xmax + 1)]))


def day14(lines: list[str], has_floor: bool) -> str:
    m = {}
    xmin, xmax = 500, 500
    for l in lines:
        for i, _ in list(enumerate(f := re.findall(r"(\d+),(\d+)", l)))[:-1]:
            for x in range(x1 := int(f[i][0]), (x2 := int(f[i + 1][0])) + (s := 1 if x2 >= x1 else -1), s):
                for y in range(y1 := int(f[i][1]), (y2 := int(f[i + 1][1])) + (s := 1 if y2 >= y1 else -1), s):
                    if not m.get(y):
                        m[y] = set()
                    m[y].add(x)
                    xmin, xmax = min(xmin, x), max(xmax, x)
    ymax = max(m.keys())

    if has_floor:
        ymax += 2
        xmin -= ymax
        xmax += ymax
        m[ymax] = set()
        for x in range(xmin, xmax + 1):
            m[ymax].add(x)

    w = copy.deepcopy(m)

    print_map(print_start, w, m, xmin, xmax, ymax)

    count = 0
    x, y = 500, 0
    while True:
        if y == ymax:
            print_map(print_result, w, m, xmin, xmax, ymax)
            return str(count)
        elif y + 1 in m:
            if not x in (yy := m[y + 1]):
                y += 1
            elif not x - 1 in yy:
                x -= 1
                y += 1
            elif not x + 1 in yy:
                x += 1
                y += 1
            else:
                if not m.get(y):
                    m[y] = set()
                m[y].add(x)
                xmin, xmax = min(xmin, x), max(xmax, x)
                count += 1

                if has_floor and y == 0:
                    print_map(print_result, w, m, xmin, xmax, ymax)
                    return str(count)

                x, y = 500, 0
        else:
            y += 1


def day14a(lines: list[str]) -> str:
    return day14(lines, False)


def day14b(lines: list[str]) -> str:
    return day14(lines, True)
