def day18_next_blocks(x, y, z, m):
    return [(u, v, w) for (u, v, w) in [(x + 1, y, z), (x - 1, y, z), (x, y + 1, z), (x, y - 1, z), (x, y, z + 1), (x, y, z - 1)] if 0 <= u < m and 0 <= v < m and 0 <= w < m]


def day18_add_block(a, x, y, z, m):
    a[x][y][z] = 6
    for u, v, w in day18_next_blocks(x, y, z, m):
        if a[u][v][w] > 0:
            a[x][y][z] -= 1
            a[u][v][w] -= 1


def day18_print_blocks(a, m):
    for x in range(m):
        for y in range(m):
            for z in range(m):
                print(" " if type(a[x][y][z]) is bool else str(a[x][y][z]), end="")
            print()
        print("-----")


def day18(lines: list[str], ext: bool) -> str:
    m = max([max(int(x) for x in line.split(",")) for line in lines]) + 1
    a = [[[False] * m for _ in range(m)] for _ in range(m)]

    for line in lines:
        x, y, z = [int(i) for i in line.split(",")]
        day18_add_block(a, x, y, z, m)

    if ext:
        empties = {(x, y, z) for x, ax in enumerate(a) for y, ay in enumerate(ax) for z, az in enumerate(ay) if type(az) is bool}
        while empties:
            todo = {empties.pop()}
            done = set()
            air = False

            while todo:
                x, y, z = todo.pop()
                done.add((x, y, z))
                if x == 0 or x == m - 1 or y == 0 or y == m - 1 or z == 0 or z == m - 1:
                    air = True
                for u, v, w in day18_next_blocks(x, y, z, m):
                    if type(a[u][v][w]) is bool and (u, v, w) not in done and (u, v, w) not in todo:
                        todo.add((u, v, w))
                        empties.remove((u, v, w))

            if not air:
                for x, y, z in done:
                    day18_add_block(a, x, y, z, m)

    return str(sum(a[x][y][z] for x in range(m) for y in range(m) for z in range(m)))


def day18a(lines: list[str]) -> str:
    return day18(lines, False)


def day18b(lines: list[str]) -> str:
    return day18(lines, True)
