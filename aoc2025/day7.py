def part_1(input_data: list[str]) -> int:
    result = 0
    rows = [list(l) for l in input_data]
    beams_indices = [i for i in range(len(rows[0])) if rows[0][i] == "S"]

    for row in rows[1:]:
        splitters_indices = [i for i in range(len(row)) if row[i] == "^"]
        new_beams_indices = []
        for i in splitters_indices:
            if i in beams_indices:
                result += 1
                if i - 1 >= 0:
                    new_beams_indices.append(i - 1)
                if i + 1 < len(row):
                    new_beams_indices.append(i + 1)
        if new_beams_indices:
            beams_indices = new_beams_indices + [
                i for i in beams_indices if i not in splitters_indices
            ]

    return result


def part_2(input_data: list[str]) -> int:
    rows = [list(l) for l in input_data]
    start_idx = next(i for i in range(len(rows[0])) if rows[0][i] == "S")
    timeline_counts = {start_idx: 1}

    for row in rows[1:]:
        splitters_indices = {i for i in range(len(row)) if row[i] == "^"}
        new_counts = {}
        for pos, count in timeline_counts.items():
            if pos in splitters_indices:
                if pos - 1 >= 0:
                    new_counts[pos - 1] = new_counts.get(pos - 1, 0) + count
                if pos + 1 < len(row):
                    new_counts[pos + 1] = new_counts.get(pos + 1, 0) + count
            else:
                new_counts[pos] = new_counts.get(pos, 0) + count
        timeline_counts = new_counts

    return sum(timeline_counts.values())


if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        input_data = f.readlines()
        print(part_1(input_data))
        print(part_2(input_data))
