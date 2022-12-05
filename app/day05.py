def day05a(lines: list[str]):
    # Parsing
    sep = lines.index("")
    start, procedure = lines[: sep - 1], lines[sep + 1 :]
    stacks = [[]] + [
        [
            letter
            for line in reversed(start)
            for letter in line[4 * i + 1]
            if letter != " "
        ]
        for i in range((len(start[0]) + 1) // 4)
    ]

    # Rearrangment
    for move in procedure:
        (n, source, dest) = [int(c) for c in move.split(" ") if c.isnumeric()]
        stacks[dest] += reversed(stacks[source][-n:])
        stacks[source] = stacks[source][:-n]

    print("".join([stack.pop() for stack in stacks[1:]]))


def day05b(lines: list[str]):
    # Parsing
    sep = lines.index("")
    start, procedure = lines[: sep - 1], lines[sep + 1 :]
    stacks = [[]] + [
        [
            letter
            for line in reversed(start)
            for letter in line[4 * i + 1]
            if letter != " "
        ]
        for i in range((len(start[0]) + 1) // 4)
    ]

    # Rearrangment
    for move in procedure:
        (n, source, dest) = [int(c) for c in move.split(" ") if c.isnumeric()]
        stacks[dest] += stacks[source][-n:]
        stacks[source] = stacks[source][:-n]

    print("".join([stack.pop() for stack in stacks[1:]]))
