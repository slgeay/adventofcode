import heapq

E, S, W, N, X = ">", "v", "<", "^", "X"
MOVES = {E: (0, 1), S: (1, 0), W: (0, -1), N: (-1, 0), X: (0, 0)}
LOG = False


def day24a(lines: list[str]) -> str:
    return day24(lines)


def day24b(lines: list[str]) -> str:
    return day24(lines, True)


def log(round: int, h: int, w: int, start: int, end: int, blizzards: dict[tuple[int, int] : list[str]]) -> None:
    if LOG:
        print(f"Round {round}")
        for x in range(-1, h + 1):
            for y in range(-1, w + 1):
                if y in (-1, w) or x == -1 and y != start or x == h and y != end:
                    print("#", end="")
                elif (x, y) in blizzards:
                    print(b[0] if (l := len(b := blizzards[(x, y)])) == 1 else l, end="")
                else:
                    print(".", end="")
            print()
        print()


def day24(lines: list[str], snack: bool = False) -> str:
    h, w = len(lines) - 2, len(lines[0]) - 2
    start, end = lines[0].find(".") - 1, lines[-1].find(".") - 1
    p = (-1, start)

    blizzards = {(x, y): [d] for x, line in enumerate(lines[1:-1]) for y, d in enumerate(line[1:-1]) if d in MOVES}
    r = current_round = 0

    log(current_round, h, w, start, end, blizzards)

    goals = [(h, end)]
    if snack:
        goals += [(-1, start), (h, end)]

    queue = []

    for goal in goals:
        print("Next goal:", goal)
        heapq.heappush(queue,(r + 1, p))
        seen = set()

        while queue:
            q = heapq.heappop(queue)
            if q in seen:
                continue
            seen.add(q)
            r, (px, py) = q

            if r > current_round:
                next_blizzards = {}
                for x, y in blizzards:
                    for d in blizzards[(x, y)]:
                        dx, dy = MOVES[d]
                        next_blizzards[(nx, ny)] = next_blizzards.get((nx := (x + dx) % h, ny := (y + dy) % w), []) + [d]

                blizzards = next_blizzards
                current_round += 1
                log(current_round, h, w, start, end, blizzards)

            for dx, dy in MOVES.values():
                nx, ny = px + dx, py + dy
                if (nx, ny) == goal:
                    print("Goal", goal, "in", current_round, "rounds")
                    p, r, queue = (nx, ny), r + 1, []
                    break

                elif ((dx, dy) == (0, 0) or 0 <= nx < h and 0 <= ny < w) and not (nx, ny) in blizzards:
                    heapq.heappush(queue,(r + 1, (nx, ny)))

    return str(current_round)
