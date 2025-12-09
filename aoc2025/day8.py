from itertools import combinations
from collections import Counter


def find(parent: dict, x: int) -> int:
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent: dict, a: int, b: int) -> None:
    parent[find(parent, a)] = find(parent, b)


def parse_and_build_edges(input_data: list[str]):
    coords = [tuple(map(int, l.strip().split(","))) for l in input_data if l.strip()]
    edges = []
    for i, j in combinations(range(len(coords)), 2):
        dist = sum((a - b) ** 2 for a, b in zip(coords[i], coords[j]))
        edges.append((dist, i, j))
    edges.sort()
    return coords, edges


def part_1(input_data: list[str]) -> int:
    coords, edges = parse_and_build_edges(input_data)
    parent = {i: i for i in range(len(coords))}

    # Kruskal on the first 1000 edges
    for _, i, j in edges[:1000]:
        union(parent, i, j)

    circuit_sizes = Counter(find(parent, i) for i in range(len(coords)))
    top_3 = sorted(circuit_sizes.values(), reverse=True)[:3]

    result = 1
    for size in top_3:
        result *= size
    return result


def part_2(input_data: list[str]) -> int:
    coords, edges = parse_and_build_edges(input_data)
    parent = {i: i for i in range(len(coords))}

    # Kruskal on the full graph
    for _, i, j in edges:
        if find(parent, i) != find(parent, j):
            union(parent, i, j)
            if len(set(find(parent, k) for k in range(len(coords)))) == 1:
                return coords[i][0] * coords[j][0]

    return 0


if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        input_data = f.readlines()
        print(part_1(input_data))
        print(part_2(input_data))
