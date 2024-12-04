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

def solve_part1(data):
    return count_occurrences(data, DIRECTIONS, "XMAS")

def solve_part2(data):
    pass

def count_occurrences(data, directions, word):
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

if __name__ == "__main__":
    with open("../Inputs/Eday04.txt") as f:
        input_data = f.read()
    print("Part 1:", solve_part1(input_data))
    print("Part 2:", solve_part2(input_data))