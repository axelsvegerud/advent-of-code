def solve_part1(data):
    ordering_rules, updates = parse_input(data)
    correct_ordered_updates = find_correct_ordered_updates(ordering_rules, updates)
    middle_pages = find_middle_pages(correct_ordered_updates)
    return sum(middle_pages)

def solve_part2(data):
    ordering_rules, updates = parse_input(data)
    incorrect_ordered_updates = find_incorrect_ordered_updates(ordering_rules, updates)
    reordered_updates = [reorder_pages(ordering_rules, update) for update in incorrect_ordered_updates]
    middle_pages = find_middle_pages(reordered_updates)
    return sum(middle_pages)

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

def find_incorrect_ordered_updates(ordering_rules, updates):
    incorrect_ordered_updates = []
    for update in updates:
        if not check_ordering_rules(ordering_rules, update):
            incorrect_ordered_updates.append(update)
    return incorrect_ordered_updates

def check_ordering_rules(rules, pages):
    for x, y in rules:
        if x in pages and y in pages and pages.index(x) > pages.index(y):
            return False
    return True

def reorder_pages(rules, pages):
    reordered = True
    while reordered:
        reordered = False
        for x, y in rules:
            if x in pages and y in pages:
                x_index, y_index = pages.index(x), pages.index(y)
                if x_index > y_index:
                    pages[x_index], pages[y_index] = pages[y_index], pages[x_index]
                    reordered = True
    return pages

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