def solve_part1(data):
    calibration_equations = data.splitlines()
    calibration_result = 0

    for equation in calibration_equations:
        test_value = int(equation[:equation.index(":")])
        equation_numbers = equation[equation.index(":") + 2:].split(" ")
        valid_equations = find_valid_equations(test_value, equation_numbers)

        if valid_equations:
            calibration_result += test_value

    return calibration_result

def solve_part2(data):
    # Implement solution for part 2
    pass

def find_valid_equations(test_value, equation_numbers):
    valid_equations = []
    generate_equations(equation_numbers, 1, equation_numbers[0], valid_equations, test_value)
    return valid_equations

def generate_equations(equation_numbers, index, current_equation, valid_equations, test_value):
    operators = ['+', '*']
    if index == len(equation_numbers):
        if evaluate_equation(current_equation) == int(test_value):
            valid_equations.append(current_equation)
        return

    for operator in operators:
        generate_equations(equation_numbers, index + 1, current_equation + ' ' + operator + ' ' + equation_numbers[index], valid_equations, test_value)

def evaluate_equation(equation):
    elements = equation.split()
    result = int(elements[0])
    i = 1
    while i < len(elements):
        operator = elements[i]
        next_number = int(elements[i + 1])
        if operator == '+':
            result += next_number
        elif operator == '*':
            result *= next_number
        i += 2
    return result

if __name__ == "__main__":
    with open('../Inputs/day07.txt') as f:
        input_data = f.read()
    print("Part 1:", solve_part1(input_data))
    print("Part 2:", solve_part2(input_data))