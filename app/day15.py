import re


def day15a(lines: list[str]) -> str:
    y = int(lines[0])
    r = []
    bb = []
    for l in lines[1:]:
        (sx, sy), (bx, by) = re.findall(r"x=(-?\d+), y=(-?\d+)", l)
        if int(by) == y:
            bb.append(int(bx))
        d = abs(int(sx) - int(bx)) + abs(int(sy) - int(by))
        dx = d - abs(y - int(sy))
        if dx >= 0:
            r.append((int(sx) - dx, int(sx) + dx))

    min_x, max_x = min([x[0] for x in r]), max([x[1] for x in r])
    return str(sum([any([x >= a[0] and x <= a[1] and not x in bb for a in r]) for x in range(min_x, max_x + 1)]))


def merge(a, b, overlaps):
    if a[1] < b[0] - 1 or b[1] < a[0] - 1:
        return False
    if (o := min(a[1], b[1]) - max(a[0], b[0])) >= 0:
        overlaps.add(o)
    return (min(a[0], b[0]), max(a[1], b[1]))


def day15b(lines: list[str]) -> str:
    maxy = int(lines[0]) * 2
    sensors = [(int(sx), int(sy), abs(int(sx) - int(bx)) + abs(int(sy) - int(by))) for (sx, sy), (bx, by) in [re.findall(r"x=(-?\d+), y=(-?\d+)", l) for l in lines[1:]]]

    y = 0
    while y <= maxy:
        intervals = {(sx - dx, sx + dx) for sx, sy, d in sensors if (dx := d - abs(y - sy)) >= 0}
        result, overlaps = set(), set()
        while intervals:
            found = False
            i = intervals.pop()
            for i2 in intervals:
                if n := merge(i, i2, overlaps):
                    intervals.remove(i2)
                    intervals.add(n)
                    found = True
                    break
            if not found:
                result.add(i)

        if len(result) == 2:
            return str((min([i[1] for i in result]) + 1) * 4000000 + y)

        i = result.pop()
        overlaps.add(0 - i[0])
        overlaps.add(i[1] - maxy)
        y += max(1, min(overlaps) // 2)
