def total_points(data):
    points = 0
    card_matches = matches(data)

    for card in card_matches:
        if len(card[1]) == 1:
            points += 1
        elif len(card[1]) > 1:
            points += 2 ** (len(card[1]) - 1)

    return points

def count_copies(data):
    pass

def matches(data):
    matches = []
    for card in data:
        card_splitted = card.split(": ")
        card_number = card_splitted[0][-1]
        card_splitted = card_splitted[1].split(" | ")
        winning_numbers = card_splitted[0].split(" ")
        player_numbers = card_splitted[1].split(" ")

        winning_numbers = [num for num in winning_numbers if num != '']
        player_numbers = [num for num in player_numbers if num != '']

        matches.append([card_number, [num for num in winning_numbers if num in player_numbers]])
        
    return matches

def main(inputfile):

    data = []
    part_one = 0
    with open(inputfile, 'r') as file:
        data = [line.strip() for line in file.read().splitlines()]
        

    return total_points(data), None