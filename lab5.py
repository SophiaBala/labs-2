def read_from_file(file_name):
    with open(file_name, 'r') as file:
        matrix = []
        for line in file:
            matrix.append(list(map(str, map(str.strip, line.strip().split(", ")))))

    return matrix

def to_file(matrix):
    with open("modified_matrix.txt", 'w') as file:
        for line in matrix:
            file.write(", ".join(line) + "\n")

def print_matrix(matrix):
    for row in matrix:
        print(", ".join(row))
    print()

def flood_fill(matrix, n, m, new_color):
    rows, cols = len(matrix), len(matrix[0])
    original_color = matrix[n][m]

    if original_color == new_color:
        return matrix

    queue = [(n, m)]

    while queue:
        x, y = queue.pop(0)

        matrix[x][y] = new_color

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1),
                       (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] == original_color:
                queue.append((nx, ny))

    return matrix


def main():
    file_name = "matrix.txt"
    matrix = read_from_file(file_name)

    print("Original Matrix:")
    print_matrix(matrix)

    while True:
        try:
            n = int(input("Enter row index (n): "))
            m = int(input("Enter column index (m): "))
            new_color = input("Enter new color: ")

            if 0 <= n < len(matrix) and 0 <= m < len(matrix[0]):
                break
            else:
                print("Invalid coordinates. Try again.\n")
        except ValueError:
            print("Please enter valid integers for n and m.\n")

    flood_fill(matrix, n, m, new_color)
    to_file(matrix)

    print("Modified Matrix:")
    print_matrix(matrix)


if __name__ == "__main__":
    main()
