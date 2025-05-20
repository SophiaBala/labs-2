def read_matrix_from_csv(filename):
    matrix = []
    with open(filename, "r") as file:
        for line in file:
            row = line.strip().split(',')
            converted_row = []
            for cell in row:
                cell = cell.strip().lower()
                if cell == "-1":
                    converted_row.append(9999999)
                else:
                    converted_row.append(float(cell))
            matrix.append(converted_row)
    return matrix

def prim_algorithm(matrix):
    n = len(matrix)
    visited = [False] * n
    min_edge = [9999999] * n
    min_edge[0] = 0
    total_length = 0

    for el in range(n):
        u = -1

        for i in range(n):
            if not visited[i] and u == -1:
                u = i

        if min_edge[u] == 9999999:
            print("No connections")
            return None

        visited[u] = True
        total_length += min_edge[u]

        for v in range(n):
            if not visited[v] and matrix[u][v] < min_edge[v]:
                min_edge[v] = matrix[u][v]
    return total_length

matrix = read_matrix_from_csv("islands.txt")
result = prim_algorithm(matrix)

if result is not None:
    print("Min length:", result)