# For this one I used Numpy to do some matrix transpositions
import numpy as np


def part_1(input_data) -> int:
    operators = input_data[-1].split()
    values = np.array([l.split() for l in input_data[:-1]], dtype=int).T

    return np.array(
        [
            np.sum(row) if op == "+" else np.prod(row)
            for row, op in zip(values, operators)
        ]
    ).sum()


def part_2(input_data) -> int:
    operators = input_data[-1].split()
    # Replacing spaces by underscores for easier debugging
    values = np.array(
        [list(l.replace(" ", "_").strip()) for l in input_data], dtype=str
    ).T.tolist()

    groups = []
    current_group = []

    for row in values:
        if len(np.unique(row)) == 1:  # Means this is a separator row
            groups.append(current_group)
            current_group = []
        else:
            num = int("".join(c for c in row if c.isdigit()))
            current_group.append(num)

    groups.append(current_group)

    ops = {"+": sum, "*": np.prod}
    return sum(ops[op](group) for group, op in zip(groups, operators))


if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        input_data = f.readlines()
        print(part_1(input_data))
        print(part_2(input_data))
