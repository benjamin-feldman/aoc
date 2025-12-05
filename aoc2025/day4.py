def is_accessible(i: int, j: int, grid: list[list[int]]) -> bool:
    neighbours_count = 0

    m, n = len(grid), len(grid[0])
    neighbour_indices: list[tuple[int, int]] = [
        (i + 1, j),
        (i, j + 1),
        (i + 1, j + 1),
        (i - 1, j - 1),
        (i - 1, j),
        (i, j - 1),
        (i + 1, j - 1),
        (i - 1, j + 1),
    ]

    for ii, jj in neighbour_indices:
        if (not 0 <= ii < m) or (not 0 <= jj < n):
            continue

        if grid[ii][jj] == 1:
            neighbours_count += 1

    return neighbours_count < 4


def part_1(grid: list[list[int]]) -> bool:
    result = 0
    m, n = len(grid), len(grid[0])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                result += is_accessible(i, j, grid)

    return result


def part_2(grid: list[list[int]]) -> bool:
    result = 0
    m, n = len(grid), len(grid[0])

    last_accessible = 1
    current_grid = grid.copy()

    while last_accessible > 0:
        current_accessible = 0
        accessible_indices: list[tuple[int, int]] = []

        for i in range(m):
            for j in range(n):
                if current_grid[i][j] == 1 and is_accessible(i, j, current_grid):
                    current_accessible += 1
                    accessible_indices.append((i, j))

        for i, j in accessible_indices:
            current_grid[i][j] = 0

        result += current_accessible

        last_accessible = current_accessible

    return result


if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        input_data = f.readlines()
        # Converting the "@" as 1 and "." as 0 for clarity
        grid = [[1 if i == "@" else 0 for i in list(l.strip("\n"))] for l in input_data]
        print(part_1(grid))
        print(part_2(grid))
