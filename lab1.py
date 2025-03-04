
import unittest

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


class zigzagtest(unittest.TestCase):

    def test_matrix(self):
        matrix = [
            [1, 2, 6],
            [3, 5, 7],
            [4, 8, 9]
        ]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = zigzag(matrix)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
