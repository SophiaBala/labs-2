with open("tiles.txt", "r") as f:
    lines = f.read().splitlines()

W, H = map(int, lines[0].split())

grid = []
for i in range(1, H + 1):
    grid.append(lines[i])

ways = []
for y in range(H):
    row = []
    for x in range(W):
        row.append(0)
    ways.append(row)


for y in range(H):
    ways[y][0] = 1


all_same = all(cell == grid[0][0] for row in grid for cell in row)

if all_same:
    for x in range(W - 1):
        total = sum(ways[y][x] for y in range(H))
        for xx in range(x + 1, W):
            for yy in range(H):
                ways[yy][xx] += total

else:
    for x in range(W - 1):
        for y in range(H):
            value = ways[y][x]
            if value == 0:
                continue

            current_letter = grid[y][x]

            for yy in range(H):
                for xx in range(x + 2, W):
                    if grid[yy][xx] == current_letter:
                        ways[yy][xx] += value

            ways[y][x + 1] += value

            if y > 0 and grid[y - 1][x + 1] == current_letter:
                ways[y - 1][x + 1] += value

            if y < H - 1 and grid[y + 1][x + 1] == current_letter:
                ways[y + 1][x + 1] += value


print("Ways:")
for row in ways:
    print(row)

result = 0
if H == 1:
    result = ways[0][W - 1]
else:
    result = ways[0][W - 1] + ways[H - 1][W - 1]

print("Amount of ways:", result)