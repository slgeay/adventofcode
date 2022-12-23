LOG = False


def log(round: int, elves: set[tuple[int, int]]) -> None:
    if LOG:
        print(f"Round {round}")
        for x in range(min(x for x, _ in elves), max(x for x, _ in elves) + 1):
            for y in range(min(y for _, y in elves), max(y for _, y in elves) + 1):
                print("#" if (x, y) in elves else ".", end="")
            print()


def day23a(lines: list[str]) -> str:
    return day23(lines, 10)


def day23b(lines: list[str]) -> str:
    return day23(lines, 0)


def day23(lines: list[str], max_rounds: int) -> str:
    elves = {(x, y) for x in range(len(lines)) for y in range(len(lines[x])) if lines[x][y] == "#"}
    neighbors = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if x != 0 or y != 0]
    moves = [(x, y) for x in [-1, 1, 0] for y in [0, -1, 1] if bool(x) != bool(y)]
    horizontal = [(0, y) for y in range(-1, 2)]
    vertical = [(x, 0) for x in range(-1, 2)]

    round = 0
    log(round, elves)

    while True:
        round += 1
        propositions: dict[tuple, list[tuple]] = dict()

        for (x, y) in elves:
            if not any((x + dx, y + dy) in elves for dx, dy in neighbors):
                continue

            for dx, dy in moves:
                if not any((x + dx + ddx, y + dy + ddy) in elves for ddx, ddy in (horizontal if dy == 0 else vertical)):
                    propositions[(x + dx, y + dy)] = propositions.get((x + dx, y + dy), []) + [(x, y)]
                    break

        if not propositions:
            break

        for (nx, ny) in propositions:
            if len(p := propositions[(nx, ny)]) == 1:
                elves.remove(p.pop())
                elves.add((nx, ny))

        log(round, elves)

        moves.append(moves.pop(0))

        if round == max_rounds:
            break

    return str((1 + max(x for x, _ in elves) - min(x for x, _ in elves)) * (1 + max(y for _, y in elves) - min(y for _, y in elves)) - len(elves) if max_rounds else round)
