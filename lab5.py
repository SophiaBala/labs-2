def read_from_file(file_name):
    with open(file_name, 'r') as file:
        matrix = []
        for line in file:
            matrix.append(list(map(str, line.strip().split(", "))))
    return matrix

def to_file(matrix):
    with open("modified_matrix.txt", 'w') as file:
        for line in matrix:
            file.write(",".join(line) + "\n")

def flood_fill(grid, i, j, new_color):
    n = len(grid)
    m = len(grid[0])
    old_color = grid[i][j]
    queue = [(i, j)]
    if old_color == new_color:
        return

    while queue:
        i, j = queue.pop(0)

        if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != old_color:
            continue

        grid[i][j] = new_color

        queue.append((i + 1, j))
        queue.append((i - 1, j))
        queue.append((i, j + 1))
        queue.append((i, j - 1))


file_name = "matrix.txt"
matrix = read_from_file(file_name)
n, m, new_color = 3, 2, "'T'"
flood_fill(matrix, n, m, new_color)
to_file(matrix)


