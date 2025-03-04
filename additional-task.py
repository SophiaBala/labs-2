def zigzag(matrix):
    rows, cols = len(matrix), len(matrix[0])
    result = []
    visited = set() 

    row, col = 0, cols - 1  

    while len(result) < rows * cols:

        if (row, col) not in visited:
            result.append(matrix[row][col])
            visited.add((row, col))

        if col > 0:
            col -= 1
        else: 
            row += 1

        while row < rows and col < cols:
            if (row, col) not in visited:
                result.append(matrix[row][col])
                visited.add((row, col))
            row += 1
            col += 1

        row -= 1
        col -= 1

        if row + 1 < rows:
            row += 1
        else: 
            col -= 1

        while row >= 0 and col >= 0:
            if (row, col) not in visited:
                result.append(matrix[row][col])
                visited.add((row, col))
            row -= 1
            col -= 1

        row += 1
        col += 1

    return result  

matrix = [
    [7, 6, 2, 1],
    [13, 8, 5, 3],
    [14, 12, 9, 4],
    [16, 15, 11, 10]
]

print(zigzag(matrix))
