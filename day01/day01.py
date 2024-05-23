import string

digit_word_map = dict(
    one = 1, 
    two = 2, 
    three = 3, 
    four = 4, 
    five = 5, 
    six = 6, 
    seven = 7, 
    eight = 8, 
    nine = 9
)

def find_digit(line, reverse=False):
    
    start = 0
    stop = len(line) + 1
    step = 1
    
    if reverse:
        start = -1
        stop *= -1
        step *= -1
    
    
    for i in range(start, stop, step):
        if line[i].isdigit():
            return line[i]
        if reverse:
            substr = line[i:]
        else:
            substr = line[:i + step]
        
        for word, digit in digit_word_map.items():
            if word in substr:
                return digit

def part_one(inputfile):
    sum = 0

    with open(inputfile, 'r') as pinput:
        for line in pinput:
            digits = []
            for character in line:
                if character in string.digits:
                    digits.append(character)
            result = str(digits[0]) + str(digits[-1])
            sum += int(result)

    return sum

def part_two(inputfile):
    sum = 0
    
    with open(inputfile, 'r') as pinput:
        for line in pinput:
            first_digit = find_digit(line)
            last_digit = find_digit(line, reverse=True)
            result = str(first_digit) + str(last_digit)
            sum += int(result)

    return sum

def main(inputfile):
    try:
        return(part_one(inputfile), part_two(inputfile))
    except OSError as err:
        print(err)
