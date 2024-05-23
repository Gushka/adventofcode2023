gear_numbers = []
asterisk_positions = []
gear_parts = []

def is_symbol_nearby(data, line_index, start_column, end_column):
    if start_column > 0:
        check_start = start_column - 1
        if not data[line_index][check_start].isdigit() and data[line_index][check_start] != '.':
            return True
    else:
        check_start = 0

    if end_column == len(data[0]) - 1:
        check_end = end_column
    else:
        check_end = end_column + 1
        if not data[line_index][check_end].isdigit() and data[line_index][check_end] != '.':
            return True

    if line_index > 0:
        for i in range(check_start, check_end + 1):
            if not data[line_index - 1][i].isdigit() and data[line_index - 1][i] != '.':
                return True
    if line_index < len(data) - 1:
        for i in range(check_start, check_end + 1):
            if not data[line_index + 1][i].isdigit() and data[line_index + 1][i] != '.':
                return True

    return False

def find_asterisks(data, line_index, start_column, end_column):
    
    if start_column > 0:
        check_start = start_column - 1
        if data[line_index][check_start] == '*':
            if [line_index, check_start] in asterisk_positions:
                gear_numbers.append(int(data[line_index][start_column:end_column + 1]) * gear_parts[asterisk_positions.index([line_index, check_start])])
            else:
                asterisk_positions.append([line_index, check_start])
                gear_parts.append(int(data[line_index][start_column:end_column + 1]))
    else:
        check_start = 0
    
    if end_column == len(data[0]) - 1:
        check_end = end_column
    else:
        check_end = end_column + 1
        if data[line_index][check_end] == '*':
            if [line_index, check_end] in asterisk_positions:
                gear_numbers.append(int(data[line_index][start_column:end_column + 1]) * gear_parts[asterisk_positions.index([line_index, check_end])])

    if line_index > 0:
        for i in range(check_start, check_end + 1):
            if data[line_index - 1][i] == '*':
                if [line_index - 1, i] in asterisk_positions:
                    gear_numbers.append(int(data[line_index][start_column:end_column + 1]) * gear_parts[asterisk_positions.index([line_index - 1, i])])  
                else:
                    asterisk_positions.append([line_index - 1, i])
                    gear_parts.append(int(data[line_index][start_column:end_column + 1]))
    
    if line_index < len(data) - 1:
        for i in range(check_start, check_end + 1):
            if data[line_index + 1][i] == "*":
                if [line_index + 1, i] in asterisk_positions:
                    gear_numbers.append(int(data[line_index][start_column:end_column + 1]) * gear_parts[asterisk_positions.index([line_index + 1, i])])
                else:
                    asterisk_positions.append([line_index + 1, i])
                    gear_parts.append(int(data[line_index][start_column:end_column + 1]))

def find_part_numbers(data):
    part_numbers = []
    for line_index, line in enumerate(data):
        column = 0
        while column < len(data[0]):
            if data[line_index][column].isdigit():
                number_start = column
                column += 1
                while column < len(data[line_index]) and data[line_index][column].isdigit():
                    column += 1
                number_end = column - 1
                if is_symbol_nearby(data, line_index, number_start, number_end):
                    part_numbers.append(int(data[line_index][number_start:number_end + 1]))
            column += 1
    return part_numbers

def find_gear_parts(data):
    for line_index in range(len(data)):
        column = 0
        while column < len(data[0]):
            if data[line_index][column].isdigit():
                number_start = column
                column += 1
                while column < len(data[line_index]) and data[line_index][column].isdigit():
                    column += 1
                number_end = column - 1
                find_asterisks(data, line_index, number_start, number_end)
            column += 1
    return gear_numbers


def main(inputfile):
    data = ""
    with open(inputfile, "r") as file:
        data = [x.strip() for x in file.read().splitlines()]

    part_one = sum(find_part_numbers(data))
    find_gear_parts(data)
    part_two = sum(gear_numbers) # INCORRECT

    return part_one, None