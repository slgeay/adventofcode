E, S, W, N = 0, 1, 2, 3
LOG = False


def day22a(lines: list[str]) -> str:
    return day22(lines, False)


def day22b(lines: list[str]) -> str:
    return day22(lines, True)


def print_dir(dir):
    if dir == E:
        return "E"
    elif dir == S:
        return "S"
    elif dir == W:
        return "W"
    elif dir == N:
        return "N"


def log(*args):
    if LOG:
        print(*args)


def day22(lines: list[str], is_cube: bool) -> str:
    ### Initialize an horizontal and vertical board
    board = lines[:-2]
    draob = ["".join([b[i] if i < len(b) else " " for b in board]) for i in range(max(len(b) for b in board))]

    ### Initialize the jumps (pre-encoded in the input)
    jl = lines[-2].split(",")
    size = int(jl[0])
    if is_cube:
        jumps = {}
        for j in jl[1:]:
            jumps[(int(j[0]), int(j[1]), int(j[2]))] = (int(j[3]), int(j[4]), int(j[5]))
            jumps[(int(j[3]), int(j[4]), (int(j[5]) + 2) % 4)] = (int(j[0]), int(j[1]), (int(j[2]) + 2) % 4)

    ### Initialize the moves
    moves = lines[-1]

    ### Initialize the position and direction
    x, y, dir = 0, board[0].find("."), 0

    while moves:
        ### Parse the next move
        r, l = moves.find("R"), moves.find("L")
        i = min(r, l) if r >= 0 and l >= 0 else max(r, l)
        move = int(moves[:i] if i >= 0 else moves)
        moves = moves[i:] if i >= 0 else ""

        log("Next move", move, print_dir(dir))

        while move:
            log("From", (x, y), "move", move, "dir", print_dir(dir))
            vertical = dir in (S, N)
            forward = dir in (E, S)

            ### Setup the board and the position
            if vertical:
                b = draob[y]
                pos = x
            else:
                b = board[x]
                pos = y

            ### Find the start and end of the line
            start, end = b.find("."), b.rfind(".")
            if (wall := b.find("#")) >= 0 and wall < start:
                start = wall
            if (wall := b.rfind("#")) >= 0 and wall > end:
                end = wall

            ### Find the next wall
            i = b.find("#", pos + 1, pos + move + 1) if forward else b.rfind("#", max(0, pos - move), pos)

            ### If there is a wall in the way, stop to it
            if i >= 0:
                pos = i - 1 if forward else i + 1
                move = 0
                if vertical:
                    x = pos
                else:
                    y = pos

            ### If the move is within the board, move there
            elif pos + move <= end if forward else pos - move >= start:
                pos = pos + move if forward else pos - move
                move = 0
                if vertical:
                    x = pos
                else:
                    y = pos

            ### If the move is outside the board, jump to the next block
            else:
                move -= end - pos if forward else pos - start

                ### Move to the max and store the delta from the port side
                if dir == E:
                    y = end
                    delta = x % size
                elif dir == S:
                    x = end
                    delta = size - y % size - 1
                elif dir == W:
                    y = start
                    delta = size - x % size - 1
                elif dir == N:
                    x = start
                    delta = y % size

                if is_cube:
                    ### Find the next block
                    jump = jumps[(x // size, y // size, dir)]
                    next_x_start, next_x_end = jump[0] * size, (jump[0] + 1) * size - 1
                    next_y_start, next_y_end = jump[1] * size, (jump[1] + 1) * size - 1
                    next_dir = jump[2]

                    ### Premove to the next block
                    if next_dir == E:
                        next_x = next_x_start + delta
                        next_y = next_y_start
                    elif next_dir == S:
                        next_x = next_x_start
                        next_y = next_y_end - delta
                    elif next_dir == W:
                        next_x = next_x_end - delta
                        next_y = next_y_end
                    elif next_dir == N:
                        next_x = next_x_end
                        next_y = next_y_start + delta

                else:
                    ### Premove to the other side of the same line
                    next_dir = dir
                    if dir == E:
                        next_x = x
                        next_y = start
                    elif dir == S:
                        next_x = start
                        next_y = y
                    elif dir == W:
                        next_x = x
                        next_y = end
                    elif dir == N:
                        next_x = end
                        next_y = y

                ### If the premove is empty, move there
                if board[next_x][next_y] == ".":
                    x, y, dir, move = next_x, next_y, next_dir, move - 1

                ### If the premove is a wall, stop
                else:
                    move = 0
                    assert board[next_x][next_y] == "#", (next_x, next_y, board[next_x][next_y])

            assert board[x][y] == ".", (x, y, board[x][y])
            log("=>", (x, y), "dir", print_dir(dir))

        ### Turn
        if moves:
            dir = (dir + (1 if moves[0] == "R" else -1)) % 4
        moves = moves[1:]

    return str(1000 * (x + 1) + 4 * (y + 1) + dir)
