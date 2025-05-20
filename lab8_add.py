class MinHeap:
    def __init__(self):
        self.a = []

    def push(self, val):
        self.a.append(val)
        i = len(self.a) - 1
        while i > 0 and self.a[(i - 1) // 2][0] > self.a[i][0]:
            self.a[i], self.a[(i - 1) // 2] = self.a[(i - 1) // 2], self.a[i]
            i = (i - 1) // 2

    def pop(self):
        if not self.a:
            return None
        val = self.a[0]
        self.a[0] = self.a[-1]
        self.a.pop()
        i = 0
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i
            if left < len(self.a) and self.a[left][0] < self.a[smallest][0]:
                smallest = left
            if right < len(self.a) and self.a[right][0] < self.a[smallest][0]:
                smallest = right
            if smallest == i:
                break
            self.a[i], self.a[smallest] = self.a[smallest], self.a[i]
            i = smallest
        return val

    def decrease_key(self, key, new_val):
        for i in range(len(self.a)):
            if self.a[i][1] == key and new_val < self.a[i][0]:
                self.a[i] = (new_val, key)
                while i > 0 and self.a[(i - 1) // 2][0] > self.a[i][0]:
                    self.a[i], self.a[(i - 1) // 2] = self.a[(i - 1) // 2], self.a[i]
                    i = (i - 1) // 2
                break

    def empty(self):
        return not self.a


def read_matrix_from_csv(filename):
    matrix = []
    with open(filename, "r") as file:
        for line in file:
            row = []
            for cell in line.strip().split(","):
                cell = cell.strip().lower()
                if cell == "-1" or cell == "inf":
                    row.append(9999999)
                else:
                    row.append(float(cell))
            matrix.append(row)
    return matrix


def prim_with_heap(matrix):
    n = len(matrix)
    visited = [False] * n
    min_edge = [9999999] * n
    min_edge[0] = 0
    total_length = 0

    heap = MinHeap()
    for i in range(n):
        heap.push((min_edge[i], i)) 

    while not heap.empty():
        weight, u = heap.pop()
        if visited[u]:
            continue
        visited[u] = True
        total_length += weight

        for v in range(n):
            if not visited[v] and matrix[u][v] < min_edge[v]:
                min_edge[v] = matrix[u][v]
                heap.decrease_key(v, matrix[u][v])

    return total_length


matrix = read_matrix_from_csv("islands.txt")
length = prim_with_heap(matrix)
print("Min length:", length)
