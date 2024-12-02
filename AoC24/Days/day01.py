def solve_part1(data):
    total_distance = 0;
    left = [];
    right = [];
    
    for line in data.splitlines():
        x, y = map(int, line.split())
        left.append(x)
        right.append(y)
    
    for val in range(len(left)):
        total_distance += abs(left.pop(left.index(min(left))) - right.pop(right.index(min(right))))
        
    return total_distance

def solve_part2(data):
    # Implement solution for part 2
    pass

if __name__ == "__main__":
    with open("../Inputs/day01.txt") as f:
        input_data = f.read()
    print("Part 1:", solve_part1(input_data))
    print("Part 2:", solve_part2(input_data))