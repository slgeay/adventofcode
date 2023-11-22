def day12(lines: list[str]) -> int:
    w, h = len(lines[0]), len(lines)
    path = [[w*h]*w for _ in range(h)]
    for i in range(len(lines)):
        try:
            j = lines[i].index("E")
            break
        except ValueError:
            pass
    lines[i] = lines[i].replace("E", "z")
    path[i][j] = 0
    queue = [(i, j)]

    for (i,j) in queue:
        for u,v in [(i,j-1), (i,j+1), (i-1,j), (i+1,j)]:
            if 0 <= u < h and 0 <= v < w:
                if ord(lines[i][j]) <= ord("b") and lines[u][v] == "S":
                    return path[i][j]+1
                elif ord(lines[u][v]) >= ord(lines[i][j])-1 and path[u][v] > path[i][j]+1:
                    path[u][v] = path[i][j]+1
                    queue.append((u,v))
    return w*h


def day12a(lines: list[str]) -> str:
    return str(day12(lines))


def day12b(lines: list[str]) -> str:
    lines = [lines[i].replace("a", "S") for i in range(len(lines))]
    return str(day12(lines))
