def solve_part1(data):
    ordering_rules, updates = parse_input(data)
    correct_ordered_updates = find_correct_ordered_updates(ordering_rules, updates)
    middle_pages = find_middle_pages(correct_ordered_updates)
    return sum(middle_pages)

def solve_part2(data):
    # Implement solution for part 2
    pass

def parse_input(data):
    ordering_rules, updates = data.split("\n\n")
    ordering_rules = [tuple(map(int, rule.split("|"))) for rule in ordering_rules.splitlines()]
    updates = [list(map(int, update.split(","))) for update in updates.splitlines()]
    return ordering_rules, updates

def find_correct_ordered_updates(ordering_rules, updates):
    correct_ordered_updates = []
    for update in updates:
        if check_ordering_rules(ordering_rules, update):
            correct_ordered_updates.append(update)
    return correct_ordered_updates

def check_ordering_rules(rules, pages):
    for x, y in rules:
        if x in pages and y in pages:
            if pages.index(x) > pages.index(y):
                return False
    return True

def find_middle_pages(correct_ordered_updates):
    middle_pages = []
    for pages in correct_ordered_updates:
        middle_pages.append(pages[len(pages) // 2])
    return middle_pages

if __name__ == "__main__":
    with open("../Inputs/day05.txt") as f:
        input_data = f.read()
    print("Part 1:", solve_part1(input_data))
    print("Part 2:", solve_part2(input_data))