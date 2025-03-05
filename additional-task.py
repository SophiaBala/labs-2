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

class TestZigzag(unittest.TestCase):

    def test_matrix(self):
        matrix2x4 = [
            [7, 6, 2, 1],
            [13, 8, 5, 3],
            [14, 12, 9, 4]
        ]

        expected = [1,2,3,4,5,6,7,8,9,12,13,14]
        result = zigzag(matrix2x4)
        self.assertEqual(expected, result)

    def test_matrix5x5(self):
        matrix = [
            [1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20],
            [21,22,23,24,25]
        ]

        expected = [5,4,10,15,9,3,2,8,14,20,25,19,13,7,1,6,12,18,24,23,17,11,16,22,21]
        result = zigzag(matrix)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
