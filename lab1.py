def zigzag(matrix):
    rows, cols = len(matrix), len(matrix[0])
    result = []

    for sum_idx in range(rows + cols - 1):
        if sum_idx % 2 == 0:
            row = min(sum_idx, rows - 1)
            col = sum_idx - row
            while row >= 0 and col < cols:
                result.append(matrix[row][col])
                row -= 1
                col += 1
        else:
            col = min(sum_idx, cols - 1)
            row = sum_idx - col
            while col >= 0 and row < rows:
                result.append(matrix[row][col])
                row += 1
                col -= 1
    return result
