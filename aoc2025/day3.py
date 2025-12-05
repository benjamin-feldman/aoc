def part_1(batteries_list: list[list[int]]) -> int:
    result = 0

    for batteries in batteries_list:
        first_digit = max(batteries[:-1])
        second_digit = max(batteries[batteries.index(first_digit) + 1 :])
        result += first_digit * 10 + second_digit

    return result


def part_2(batteries_list: list[list[int]]) -> int:
    result = 0

    for batteries in batteries_list:
        joltage = 0
        last_digit_index = -1

        for i in range(11, -1, -1):
            sublist = batteries[last_digit_index + 1 : len(batteries) - i]
            current_digit = max(sublist)

            if i > 0:
                last_digit_index = (last_digit_index + 1) + batteries[
                    last_digit_index + 1 : -i
                ].index(current_digit)

            joltage += 10 ** (i) * current_digit

        result += joltage

    return result


if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        input_data = f.readlines()
        batteries_list = [[int(i) for i in list(l.strip("\n"))] for l in input_data]
        print(part_1(batteries_list))
        print(part_2(batteries_list))
