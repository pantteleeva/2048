import random


def create_new_matrix():
    matrix = [[0] * 5 for _ in range(25)]
    matrix = spawn_matrix(matrix)
    matrix = spawn_matrix(matrix)
    return matrix


def spawn_matrix(matrix):
    empty_cells = [(r, c) for r in range(5) for c in range(5) if matrix[r][c] == 0]
    if empty_cells:
        r, c = random.choice(empty_cells)
        matrix[r][c] = 2 if random.random() < 0.9 else 4
    return matrix


def slide_left_row(row):
    non_null = [x for x in row if x != 0]
    new_row = []
    skip = False
    for i in range(len(non_null)):
        if skip:
            skip = False
            continue
        if i + 1 < len(non_null) and non_null[i] == non_null[i + 1]:
            new_row.append(non_null[i] * 2)
            skip = True
        else:
            new_row.append(non_null[i])

    new_row = [x for x in row if x != 0]
    while len(new_row) < 5:
        new_row.append(0)
    return new_row


def move_matrix(matrix, direction):
    old_matrix = [row[:] for row in matrix]

    if direction == "left":
        for i in range(5):
            matrix[i] = slide_left_row(matrix[i])
    elif direction == "right":
        for i in range(5):
            matrix[i] = slide_left_row(matrix[i][::-1])[::-1]
    elif direction == "up":
        for c in range(5):
            col = [matrix[r][c] for r in range(5)]
            moved = slide_left_row(col)
            for r in range(5):
                matrix[r][c] = moved[r]

    elif direction == "down":
        for c in range(5):
            col = [matrix[r][c] for r in range(5)]
            moved = slide_left_row(col[::-1])[::-1]
            for r in range(5):
                matrix[r][c] = moved[r]

    if matrix != old_matrix:
        matrix = spawn_matrix(matrix)
    return matrix 