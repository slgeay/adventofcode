from math import prod


def day08a(lines: list[str]) -> str:
    return str(2*(len(lines[0])+len(lines))-4+sum([int(lines[i][j])>min((max([int(lines[i2][j2])for i2 in range(ia,ib)for j2 in range(ja,jb)])for ia,ib,ja,jb in[(0,i,j,j+1),(i+1,len(lines),j,j+1),(i,i+1,0,j),(i,i+1,j+1,len(lines[0]))]))for i in range(1,len(lines)-1)for j in range(1,len(lines[i])-1)]))


def day08b(lines: list[str]) -> str:
    return str(max([prod([1+(next((x[0]for x in enumerate(l)if x[1]>=int(lines[i][j])),len(l)-1))for l in([int(lines[i2][j2])for i2 in range(ia,ib,ic)for j2 in range(ja,jb,jc)]for ia,ib,ic,ja,jb,jc in[(i-1,-1,-1,j,j+1,1),(i+1,len(lines),1,j,j+1,1),(i,i+1,1,j-1,-1,-1),(i,i+1,1,j+1,len(lines[0]),1),])])for i in range(1,len(lines)-1)for j in range(1,len(lines[i])-1)]))


### Cleaner linear version ###

def day08a_cleaner_update_vis(is_visible: list[bool], vis_index: int) -> int:
    if not is_visible[vis_index]:
        is_visible[vis_index] = True
        return 1
    return 0


def day08a_cleaner_traversal(
    lines: list[str], cols: int, rows: int, is_visible: list[bool], is_forward: bool
) -> int:
    visible = 0
    start = 0 if is_forward else -1
    func = (lambda x: x) if is_forward else (lambda x: reversed(x))
    rows_maxes = [int(char) for char in lines[start]]
    for row in func(range(1, rows - 1)):
        col_max = int(lines[row][start])
        for col in func(range(1, cols - 1)):
            value, vis_index = int(lines[row][col]), col - 1 + (row - 1) * (cols - 2)
            if value > col_max:
                visible += day08a_cleaner_update_vis(is_visible, vis_index)
                col_max = value
            if value > int(rows_maxes[col]):
                visible += day08a_cleaner_update_vis(is_visible, vis_index)
                rows_maxes[col] = value
    return visible


def day08a_clean_linear(lines: list[str]) -> str:
    cols, rows = len(lines[0]), len(lines)
    is_visible = [False] * (cols - 2) * (rows - 2)
    return str(
        2 * (cols + rows) - 4 # Borders
        + day08a_cleaner_traversal(lines, cols, rows, is_visible, True) # Left-Down traversal
        + day08a_cleaner_traversal(lines, cols, rows, is_visible, False) # Right-Up traversal
    )
