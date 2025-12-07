def part_1(ranges: list[tuple[int, int]], ingredient_ids: list[int]) -> int:
    result = 0

    for id in ingredient_ids:
        for r in ranges:
            if r[0] <= id <= r[1]:
                result += 1
                break

    return result


def get_overlap(
    range1: tuple[int, int], range2: tuple[int, int]
) -> tuple[int, int] | None:
    """Returns merged range if ranges overlap, None otherwise"""
    start1, end1 = range1
    start2, end2 = range2
    if max(start1, start2) <= min(end1, end2):
        return (min(start1, start2), max(end1, end2))
    return None


def part_2(ranges: list[tuple[int, int]]) -> int:
    merged_ranges = ranges.copy()

    # This could be more elegant
    while True:
        new_merged_ranges = []
        merged_indices = set()
        found_overlap = False

        for i, range1 in enumerate(merged_ranges):
            for j, range2 in enumerate(merged_ranges):
                if i == j:
                    continue

                overlap = get_overlap(range1, range2)

                if overlap is not None:
                    new_merged_ranges.append(overlap)
                    merged_indices.add(i)
                    merged_indices.add(j)
                    found_overlap = True
                    break

        for i, r in enumerate(merged_ranges):
            if i not in merged_indices:
                new_merged_ranges.append(r)

        new_merged_ranges = list(set(new_merged_ranges))
        merged_ranges = new_merged_ranges

        if not found_overlap:
            break

    return sum(end - start + 1 for start, end in merged_ranges)


if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        input_data = f.readlines()
        ranges = []
        ingredient_ids = []

        parse_range = lambda s: tuple(map(int, s.split("-")))

        for l in input_data:
            if "-" in l:
                ranges.append(parse_range(l))

            if l.strip().isdigit():
                ingredient_ids.append(int(l))

        print(part_1(ranges, ingredient_ids))
        print(part_2(ranges))
