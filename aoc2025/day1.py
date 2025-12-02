def part_1(initial_position: int, input_data: list[str]) -> int:
    position = initial_position
    hits_zero = 0

    for rotation in input_data:
        direction = -1 if rotation[0] == "L" else 1
        magnitude = int(rotation[1:])
        position = (position + direction*magnitude) % 100
        hits_zero += (position == 0)

    return hits_zero

def part_2(initial_position: int, input_data: list[str]) -> int:
    position = initial_position
    points_zero = 0

    for rotation in input_data:
        direction = -1 if rotation[0] == "L" else 1
        magnitude = int(rotation[1:])
        for _ in range(magnitude):
            position = (position+direction) % 100
            if position == 0:
                points_zero += 1

    return points_zero

if __name__ == "__main__":
    with open("sequence.txt", encoding="utf-8") as f:
        input_data = f.readlines()
        input_data = [line.strip() for line in input_data]
        
    print(part_1(initial_position=50, input_data=input_data))
    print(part_2(initial_position=50, input_data=input_data))