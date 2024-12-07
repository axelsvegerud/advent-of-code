def solve_part1(data):
    grid = [list(line) for line in data.splitlines()]
    start_pos = find_start_pos(grid)
    guard_route = []
    direction = (-1, 0)  # Initial dir (^)

    """
    Walking rules:
        - If there is something directly in front of you, turn right 90 degrees.
        - Otherwise, take a step forward.
    """
    pos = start_pos
    while True:
        next_pos = move_forward(pos, direction)
        if not (0 <= next_pos[0] < len(grid)) or not (0 <= next_pos[1] < len(grid[0])):
            grid[pos[0]][pos[1]] = 'X'
            break
        if grid[next_pos[0]][next_pos[1]] == "#":
            direction = turn_right(direction)
        else:
            grid[pos[0]][pos[1]] = 'X'
            pos = next_pos

    for line in grid:
        guard_route.append("".join(line))
    guard_route = "\n".join(guard_route)
    return guard_route.count("X")

def solve_part2(data):
    grid = [list(line) for line in data.splitlines()]
    start_pos = find_start_pos(grid)
    valid_positions = []
    direction = (-1, 0)  # Initial dir (^)

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if is_invalid_position(grid, start_pos, row, col):
                continue
            if find_guard_loop(grid, start_pos, direction, (row, col)):
                valid_positions.append((row, col))
    return len(valid_positions)

def find_guard_loop(grid, start_pos, direction, obstruction):
    visited_states = set()
    position = start_pos

    while True:
        state = (position, direction)
        if state in visited_states:
            return True
        visited_states.add(state)

        next_pos = move_forward(position, direction)
        if not (0 <= next_pos[0] < len(grid)) or not (0 <= next_pos[1] < len(grid[0])):
            break
        if grid[next_pos[0]][next_pos[1]] == "#" or next_pos == obstruction:
            direction = turn_right(direction)
        else:
            position = next_pos

    return False

def find_start_pos(data):
    for row, line in enumerate(data):
        if "^" in line:
            return row, line.index("^")

def turn_right(direction):
    return direction[1], -direction[0]

def move_forward(pos, direction):
    return pos[0] + direction[0], pos[1] + direction[1]

def is_invalid_position(grid, start_pos, row, col):
    return (row, col) == start_pos or grid[row][col] == "#"

if __name__ == "__main__":
    with open('../Inputs/day06.txt') as f:
        input_data = f.read()
    print("Part 1:", solve_part1(input_data))
    print("Part 2:", solve_part2(input_data))