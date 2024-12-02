def solve_part1(data):
    total_distance = 0;
    left, right = split_data(data)
    
    while left and right:
        total_distance += abs(left.pop(left.index(min(left))) - right.pop(right.index(min(right))))
        
    return total_distance

def solve_part2(data):
    similarity_score = 0;
    left, right = split_data(data)
    
    for val in left:
        similarity_score += val * right.count(val)
    
    return similarity_score

def split_data(data):
    left = [];
    right = [];
    
    for line in data.splitlines():
        x, y = map(int, line.split())
        left.append(x)
        right.append(y)
    return left, right

if __name__ == "__main__":
    with open("../Inputs/day01.txt") as f:
        input_data = f.read()
    print("Part 1:", solve_part1(input_data))
    print("Part 2:", solve_part2(input_data))