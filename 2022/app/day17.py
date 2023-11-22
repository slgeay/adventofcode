def day17_print_board(board):
    for i in reversed(range(len(board))):
        for j in range(9):
            print("|" if j == 0 or j == 8 else "#" if board[i] & (2**j) else ".", end="")
        print()
    print()


def day17(lines: list[str], n_pieces: int) -> str:
    moves = lines[0]
    n_moves = len(moves)
    i_move, z_jump, z = 0, 0, 0

    ### pieces in binary from bottom left
    pieces = [
        [2**4 - 1],
        [2**1, 2**3 - 1, 2**1],
        [2**3 - 1, 2**2, 2**2],
        [2**0, 2**0, 2**0, 2**0],
        [2**2 - 1, 2**2 - 1]
    ]

    ### board in binary from bottom left, 2**0 being a wall
    board = [2**8 - 2]

    cache = {}

    i_piece = 0
    while i_piece < n_pieces:
        ### get the next piece and init the position
        piece = [p << 3 for p in pieces[i_piece % len(pieces)]]
        z = len(board) + 3

        while True:
            move = moves[i_move]
            i_move = (i_move + 1) % n_moves
            new_piece = [p << 1 if move == ">" else p >> 1 for p in piece]

            ### if the piece doesn't touch a wall or another piece, we move it
            if not any([p >= 2**8 or p % 2 or z + i < len(board) and p + (b := board[z + i]) != p | b for i, p in enumerate(new_piece)]):
                piece = new_piece

            new_z = z - 1
            ### if the piece touch the ground or another piece, we stop moving it
            if any([new_z + i < len(board) and p + (b := board[new_z + i]) != p | b for i, p in enumerate(piece)]):
                break
            z = new_z

        ### if the piece touch a wall or another piece, we add it to the board
        for i, p in enumerate(piece):
            if z + i < len(board):
                board[z + i] = board[z + i] | p
            else:
                board.append(p)

        ### check if we already saw this board and if so, we can skip some iterations
        key = (i_move, i_piece % len(pieces), ",".join([str(b) for b in board[-(2**7) :]]))
        if key in cache:
            cip, cz = cache[key]
            z_period = len(board) - cz
            p_period = i_piece - cip
            periods = (n_pieces - i_piece) // p_period
            z_jump += periods * z_period
            i_piece += periods * p_period
        else:
            cache[key] = (i_piece, len(board))

        i_piece += 1

    return str(z_jump + len(board) - 1)


def day17a(lines: list[str]) -> str:
    return day17(lines, 2022)


def day17b(lines: list[str]) -> str:
    return day17(lines, 1000000000000)
