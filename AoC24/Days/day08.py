import sys
from collections import defaultdict

def solve_part1(data):
    grid = data.splitlines()
    antennas = find_antennas(grid)
    antinodes = find_antinodes(grid, antennas)
    return len(antinodes)

def solve_part2(data):
    grid = data.splitlines()
    antennas = find_antennas(grid)
    antinodes = find_antinodes_part2(grid, antennas)
    return len(antinodes)

def find_antennas(grid):
    antennas = {}
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell != '.':
                antennas.setdefault(cell, []).append((x, y))
    return antennas

def find_antinodes(grid, antennas):
    antinodes = set()

    for positions in antennas.values():
        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                dx, dy = x2 - x1, y2 - y1

                antinode1 = (x1 - dx, y1 - dy)
                antinode2 = (x2 + dx, y2 + dy)

                if in_bounds(antinode1, grid):
                    antinodes.add(antinode1)
                if in_bounds(antinode2, grid):
                    antinodes.add(antinode2)

    return antinodes

def find_antinodes_part2(grid, antennas):
    antinodes = set()

    for positions in antennas.values():
        n = len(positions)
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                dx, dy = x2 - x1, y2 - y1

                antinode1 = (x1 - dx, y1 - dy)
                antinode2 = (x2 + dx, y2 + dy)

                if in_bounds(antinode1, grid):
                    antinodes.add(antinode1)
                if in_bounds(antinode2, grid):
                    antinodes.add(antinode2)

                p1 = (x1 + dx, y1 + dy)
                while in_bounds(p1, grid):
                    antinodes.add(p1)
                    p1 = (p1[0] + dx, p1[1] + dy)

                p2 = (x2 - dx, y2 - dy)
                while in_bounds(p2, grid):
                    antinodes.add(p2)
                    p2 = (p2[0] - dx, p2[1] - dy)

    return antinodes

def in_bounds(position, grid):
    x, y = position
    return 0 <= y < len(grid) and 0 <= x < len(grid[0])

if __name__ == "__main__":
    with open("../Inputs/day08.txt") as f:
        input_data = f.read()
    print("Part 1:", solve_part1(input_data))
    print("Part 2:", solve_part2(input_data))