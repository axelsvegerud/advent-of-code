DIRECTIONS = [
    (0, 1),     # Horizontal right
    (1, 0),     # Vertical down
    (1, 1),     # Diagonal down-right
    (1, -1),    # Diagonal down-left
    (0, -1),    # Horizontal left
    (-1, 0),    # Vertical up
    (-1, -1),   # Diagonal up-left
    (-1, 1),    # Diagonal up-right
]

PATTERNS = [
    [('M', -1, -1), ('S', -1, 1), ('A', 0, 0), ('M', 1, -1), ('S', 1, 1)],  # Original
    [('S', -1, -1), ('M', 1, -1), ('A', 0, 0), ('S', -1, 1), ('M', 1, 1)],  # Rotated 90 degrees
    [('S', 1, -1), ('M', 1, 1), ('A', 0, 0), ('S', -1, -1), ('M', -1, 1)],  # Rotated 180 degrees
    [('M', -1, 1), ('S', 1, 1), ('A', 0, 0), ('M', -1, -1), ('S', 1, -1)]   # Rotated 270 degrees
]

def solve_part1(data):
    return count_xmas_occurrences(data, DIRECTIONS, "XMAS")

def solve_part2(data):
    return count_x_mas_occurrences(data, PATTERNS)

def count_xmas_occurrences(data, directions, word):
    grid = data.splitlines()
    occurrences = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for dx, dy in directions:
                if check_direction(grid, word, x, y, dx, dy):
                    occurrences += 1
    return occurrences

def check_direction(grid, word, x, y, dx, dy):
    for i in range(len(word)):
        nx = x + i * dx
        ny = y + i * dy
        if not (0 <= nx < len(grid)) or not (0 <= ny < len(grid[0])) or grid[nx][ny] != word[i]:
            return False
    return True

def count_x_mas_occurrences(data, patterns):
    grid = data.splitlines()
    count = 0

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for pattern in patterns:
                if found_x_mas(grid, pattern, x, y):
                    count += 1
    return count

def found_x_mas(grid, pattern, x, y):
    max_x, max_y = len(grid), len(grid[0])
    for char, dx, dy in pattern:
        new_x, new_y = x + dx, y + dy
        if not (0 <= new_x < max_x and 0 <= new_y < max_y) or grid[new_x][new_y] != char:
            return False
    return True

if __name__ == "__main__":
    with open("../Inputs/day04.txt") as f:
        input_data = f.read()
    print("Part 1:", solve_part1(input_data))
    print("Part 2:", solve_part2(input_data))