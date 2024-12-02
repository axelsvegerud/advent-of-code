def solve_part1(data):
    number_of_safe_reports = 0
    
    for line in data.splitlines():
        numbers = get_numbers(line)
        if is_decreasing_or_increasing(numbers) and is_adjacent_levels_safe(numbers): number_of_safe_reports += 1
                
    return number_of_safe_reports

def solve_part2(data):
    number_of_safe_reports = 0
    
    for line in data.splitlines():
        numbers = get_numbers(line)
        if is_decreasing_or_increasing(numbers) and is_adjacent_levels_safe(numbers):
            number_of_safe_reports += 1
        else:
            for i in range(len(numbers)):
                temp_numbers = numbers[:i] + numbers[i + 1:]
                if is_decreasing_or_increasing(temp_numbers) and is_adjacent_levels_safe(temp_numbers):
                    number_of_safe_reports += 1
                    break
                    
    return number_of_safe_reports

def get_numbers(data):
    return list(map(int, data.split()))

def is_decreasing_or_increasing(numbers):
    return all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1)) or all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))

def is_adjacent_levels_safe(numbers):
    return all(abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1))

if __name__ == "__main__":
    with open("../Inputs/day02.txt") as f:
        input_data = f.read()
    print("Part 1:", solve_part1(input_data))
    print("Part 2:", solve_part2(input_data))