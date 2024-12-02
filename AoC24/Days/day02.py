def solve_part1(data):
    number_of_safe_reports = 0
    
    for line in data.splitlines():
        safe_report = True
        nums = list(map(int, line.split()))
        if all(x < y for x, y in zip(nums, nums[1:])) or all(x > y for x, y in zip(nums, nums[1:])):
            for i in range(len(nums) - 1):
                if abs(nums[i] - nums[i + 1]) > 3:
                    safe_report = False
                    break
            if safe_report:
                number_of_safe_reports += 1
                
    return number_of_safe_reports

def solve_part2(data):
    # Implement solution for part 2
    pass

if __name__ == "__main__":
    with open("../Inputs/day02.txt") as f:
        input_data = f.read()
    print("Part 1:", solve_part1(input_data))
    print("Part 2:", solve_part2(input_data))