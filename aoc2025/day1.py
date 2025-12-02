def parse_input_line(input_line: str) -> (int, int):
    """Returns a (direction, steps) couple, representing a single rotation.
    Example: "L37" -> (1, 37)"""

    direction = -1 if input_line[0] == "L" else 1
    steps = int(input_line[1:])

    return (direction, steps)


def part_1(initial_position: int, rotations: list[(int, int)]) -> int:
    position = initial_position
    hits_zero = 0

    for direction, steps in rotations:
        position = (position + direction * steps) % 100
        hits_zero += position == 0

    return hits_zero


def part_2(initial_position: int, rotations: list[(int, int)]) -> int:
    position = initial_position
    points_zero = sum(
        1
        for direction, steps in rotations
        for _ in range(steps)
        if (position := (position + direction) % 100) == 0
    )
    return points_zero


if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        input_data = f.readlines()
        input_data = [line.strip() for line in input_data]
        rotations = [parse_input_line(l) for l in input_data]

    print(part_1(initial_position=50, rotations=rotations))
    print(part_2(initial_position=50, rotations=rotations))
