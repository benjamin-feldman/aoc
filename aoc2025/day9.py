from itertools import combinations


def part_1(input_data: list[str]) -> int:
    tiles = [tuple(map(int, t.strip().split(","))) for t in input_data]

    result = 0

    for i, j in combinations(range(len(tiles)), 2):
        tile_i, tile_j = tiles[i], tiles[j]
        area = (abs(tile_i[0] - tile_j[0]) + 1) * (abs(tile_i[1] - tile_j[1]) + 1)
        result = max(result, area)

    return result


def part_2(input_data: list[str]) -> int:
    tiles = [tuple(map(int, t.strip().split(","))) for t in input_data if t.strip()]
    n = len(tiles)

    xs = sorted(set(x for x, y in tiles))
    ys = sorted(set(y for x, y in tiles))
    x_to_idx = {x: i for i, x in enumerate(xs)}
    y_to_idx = {y: i for i, y in enumerate(ys)}
    nx, ny = len(xs), len(ys)

    boundary = set()
    for i in range(n):
        x1, y1 = tiles[i]
        x2, y2 = tiles[(i + 1) % n]
        xi1, yi1 = x_to_idx[x1], y_to_idx[y1]
        xi2, yi2 = x_to_idx[x2], y_to_idx[y2]
        if x1 == x2:
            for yi in range(min(yi1, yi2), max(yi1, yi2) + 1):
                boundary.add((xi1, yi))
        else:
            for xi in range(min(xi1, xi2), max(xi1, xi2) + 1):
                boundary.add((xi, yi1))

    # Flood fill with BFS
    visited = set(boundary)
    queue = [(-1, -1)]
    visited.add((-1, -1))

    while queue:
        cx, cy = queue.pop(0)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ncx, ncy = cx + dx, cy + dy
            if -1 <= ncx <= nx and -1 <= ncy <= ny and (ncx, ncy) not in visited:
                visited.add((ncx, ncy))
                queue.append((ncx, ncy))

    # Valid tiles = boundary + interior (ie. not visited by flood fill)
    valid = set(boundary)
    for xi in range(nx):
        for yi in range(ny):
            if (xi, yi) not in visited:
                valid.add((xi, yi))

    # Prefix sum to check if any rectangle is valid/invalid in O(1)
    # see https://en.wikipedia.org/wiki/Summed-area_table
    prefix = [[0] * (ny + 1) for _ in range(nx + 1)]
    for i in range(nx):
        for j in range(ny):
            val = 0 if (i, j) in valid else 1
            prefix[i + 1][j + 1] = (
                val + prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j]
            )

    def count_invalid(i1, j1, i2, j2):
        a, c = min(i1, i2), max(i1, i2)
        b, d = min(j1, j2), max(j1, j2)
        return prefix[c + 1][d + 1] - prefix[a][d + 1] - prefix[c + 1][b] + prefix[a][b]

    # Final calculation, similar to part 1
    result = 0

    for i, j in combinations(range(n), 2):
        x1, y1 = tiles[i]
        x2, y2 = tiles[j]
        i1, j1 = x_to_idx[x1], y_to_idx[y1]
        i2, j2 = x_to_idx[x2], y_to_idx[y2]

        if count_invalid(i1, j1, i2, j2) == 0:
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            result = max(result, area)

    return result


if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        input_data = f.readlines()
        print(part_1(input_data))
        print(part_2(input_data))
