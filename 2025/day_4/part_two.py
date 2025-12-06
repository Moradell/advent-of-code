from pathlib import Path

input_path = Path(__file__).parent / "input.txt"

input_data = input_path.read_text(encoding="utf-8")

grid = []
for line in input_data.strip().split("\n"):
    grid.append(list(line))

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def remove_rolls(grid):
    rows, cols = len(grid), len(grid[0])
    to_remove = []

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != "@":
                continue

            neighbors = 0
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    if grid[ni][nj] == "@":
                        neighbors += 1

            if neighbors < 4:
                to_remove.append((i, j))

    for i, j in to_remove:
        grid[i][j] = "."

    return len(to_remove)


def total_removed_rolls(grid):
    total = 0

    while True:
        removed = remove_rolls(grid)
        if removed == 0:
            break
        total += removed

    return total


print(total_removed_rolls(grid))
