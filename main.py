import pprint

grid =  [
[1, 0, 0, 0, 4, 0, 0, 0, 0],
[0, 9, 2, 6, 0, 0, 3, 0, 0],
[3, 0, 0, 0, 0, 5, 1, 0, 0],
[0, 7, 0, 1, 0, 0, 0, 0, 4],
[0, 0, 4, 0, 5, 0, 6, 0, 0],
[2, 0, 0, 0, 0, 4, 0, 8, 0],
[0, 0, 9, 4, 0, 0, 0, 0, 1],
[0, 0, 8, 0, 0, 6, 5, 2, 0],
[0, 0, 0, 0, 1, 0, 0, 0, 6]
]


def find_next_empty_el(smth):
    for row in range(0, 9):
        for col in range(0, 9):
            if smth[row][col] == 0:
                return row, col


def valid(row, col, gr, value):
    start_row = row - row % 3
    start_col = col - col % 3

    if value in gr[row]:
        return False
    for el in range(9):
        if value == gr[el][col]:
            return False
    for i in range(3):
        for j in range(3):
            if gr[i + start_row][j + start_col] == value:
                return False
    return True


def solve(gr):
    find = find_next_empty_el(gr)
    if find:
        row, col = find_next_empty_el(gr)
    else:
        return True

    for value in range(1, 10):
        if valid(row, col, gr, value):
            gr[row][col] = value
            if solve(gr):
                return True
            gr[row][col] = 0
    return False


solve(grid)
pprint.pprint(grid)
