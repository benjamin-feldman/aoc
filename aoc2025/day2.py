def has_repeating_pattern(n: int, pattern_length: int) -> bool:
    num_str = str(n)
    
    if len(num_str) % pattern_length != 0 or len(num_str) == 1:
        return False
    
    pattern = num_str[:pattern_length]
    
    return int(pattern * (len(num_str) // pattern_length)) == n


def part_1(ranges: list[tuple[int, int]]) -> int:
    result = 0
    
    for start, end in ranges:
        start_str, end_str = str(start), str(end)
        
        for num in range(start, end + 1):
            num_str = str(num)
            
            if len(num_str) % 2 != 0:
                continue
            
            if len(start_str) % 2 == 0 and has_repeating_pattern(num, len(start_str) // 2):
                result += num
                continue
            
            if len(end_str) % 2 == 0 and has_repeating_pattern(num, len(end_str) // 2):
                result += num
                
    return result


def part_2(ranges: list[tuple[int, int]]) -> int:
    result = 0
    
    for start, end in ranges:
        start_str, end_str = str(start), str(end)
        max_pattern_length = max(len(start_str), len(end_str)) // 2
        
        for num in range(start, end + 1):
            for pattern_length in range(1, max_pattern_length + 1):
                if len(start_str) % pattern_length != 0 and len(end_str) % pattern_length != 0:
                    continue
                
                if has_repeating_pattern(num, pattern_length):
                    result += num
                    break
                
    return result

if __name__ == "__main__":
    with open("input.txt", encoding="utf-8") as f:
        input_data = f.readline()
        parse_range = lambda s: tuple(map(int, s.split("-")))
        ranges = [parse_range(r) for r in input_data.split(",")]
        
        print(part_1(ranges))
        print(part_2(ranges))
