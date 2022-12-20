def day20_mix(l: list[str], r = 1, f = 1) -> list[int]:
    n = len(l)
    l = [int(i)*f for i in l]
    indexes = [i for i in range(n)]

    for _ in range(r):
        for ii in range(n):
            i = indexes.index(ii)
            a = l.pop(i)
            j = (i + a) % (n-1)
            indexes.pop(i)
            l.insert(j, a)
            indexes.insert(j, ii)
    return l


def day20a(lines: list[str]) -> str:
    return str((l := day20_mix(lines))[(1000 + (z := l.index(0))) % len(l)] + l[(2000 + z) % len(l)] + l[(3000 + z) % len(l)])


def day20b(lines: list[str]) -> str:
    return str((l := day20_mix(lines, 10, 811589153))[(1000 + (z := l.index(0))) % len(l)] + l[(2000 + z) % len(l)] + l[(3000 + z) % len(l)])
