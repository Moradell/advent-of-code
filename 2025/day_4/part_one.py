from pathlib import Path

input_path = Path(__file__).parent / "input.txt"

input_data = input_path.read_text(encoding="utf-8")

grid = []
for line in input_data.strip().split("\n"):
    grid.append(list(line))

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def total_accesed_rolls(grid):
    count = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "@":
                neigbors = 0

                for ni, nj in directions:
                    ni, nj = i + ni, j + nj

                    if 0 <= ni < rows and 0 <= nj < cols:
                        if grid[ni][nj] == "@":
                            neigbors += 1

                if neigbors < 4:
                    count += 1

    return count


print(total_accesed_rolls(grid))
