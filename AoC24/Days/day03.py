import re

def solve_part1(data):
    sum_of_results = 0

    for mul in find_mul(data):
        sum_of_results += evaluate_mul(mul)

    return sum_of_results

def solve_part2(data):
    sum_of_results = 0
    disable = False
    instructions = find_instructions(data)

    for instruction in instructions:
        if "don't" in instruction:
            disable = True
        elif "do" in instruction:
            disable = False

        if "mul" in instruction and not disable:
            sum_of_results += evaluate_mul(instruction)

    return sum_of_results

def evaluate_mul(expression):
    nums = re.findall(r"\d+", expression)
    return int(nums[0]) * int(nums[1])

def find_mul(data):
    return re.findall(r"mul\(\d+,\d+\)", data)

def find_instructions(data):
    return re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", data)

if __name__ == "__main__":
    with open("../Inputs/day03.txt") as f:
        input_data = f.read()
    print("Part 1:", solve_part1(input_data))
    print("Part 2:", solve_part2(input_data))