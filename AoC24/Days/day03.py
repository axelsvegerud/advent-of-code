import re

def solve_part1(data):
    sum_of_results = 0

    for mul in find_mul(data):
        nums = re.findall(r"\d+", mul)
        result = int(nums[0]) * int(nums[1])
        sum_of_results += result

    return sum_of_results

def solve_part2(data):
    # Implement solution for part 2
    pass

def find_mul(data):
    return re.findall(r"mul\(\d+,\d+\)", data)

if __name__ == "__main__":
    with open("../Inputs/day03.txt") as f:
        input_data = f.read()
    print("Part 1:", solve_part1(input_data))
    print("Part 2:", solve_part2(input_data))