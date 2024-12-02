import os
import sys
from Days import day01
from utils.helpers import get_input

def main(day):
    print(f"Day {day} Solutions:")
    data = get_input(day)
    print("Part 1:", day01.solve_part1(data))
    print("Part 2:", day01.solve_part2(data))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <day>")
        sys.exit(1)
    day = int(sys.argv[1])
    main(day)