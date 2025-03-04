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

#m == n ==5,    m =2, n =4,      n = 1, m = 6,      n == m == 1
class zigzagtest(unittest.TestCase):

    def test_matrix5x5(self):
        matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        expected = [1,2,6,11,7,3,4,8,12,16,21,17,13,9,5,10,14,18,22,23,19,15,20,24,25]
        result = zigzag(matrix)
        self.assertEqual(result, expected)

    def test_matrix2x4(self):
        matrix = [
            [1,2,3,4],
            [5,6,7,8]
        ]
        expected = [1,2,5,6,3,4,7,8]
        result = zigzag(matrix)
        self.assertEqual(result, expected)

    def test_matrix1x6(self):
        matrix = [
            [1,2,3,4,5,6]
        ]
        expected = [1,2,3,4,5,6]
        result = zigzag(matrix)
        self.assertEqual(result, expected)

    def test_matrix1x1(self):
        matrix = [
            [1]
        ]
        expected = [1]
        result = zigzag(matrix)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
