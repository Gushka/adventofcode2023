import functools

def is_game_possible(max_revealed):
    max_red = 12
    max_green = 13
    max_blue = 14
        
    return max_revealed['red'] <= max_red and max_revealed['green'] <= max_green and max_revealed['blue'] <= max_blue

def powerof_marbles(max_revealed):
    return functools.reduce(lambda x, y: x * y, list(max_revealed.values()))

def parse_game(inputfile):
    sum = 0
    power_sum = 0

    with open(inputfile, "r") as file:
        for game in file:
            game_id, game_info = game.split(": ")
            game_id = int(game_id.split(" ")[1])
            reveals = game_info.replace("\n", "").split("; ")

            max_revealed = {"red": 0, "green": 0, "blue": 0}
            for reveal in reveals:
                for part in reveal.split(", "):
                    marbles_n, color = part.split(" ")
                    max_revealed[color] = max(max_revealed[color], int(marbles_n))

            if is_game_possible(max_revealed):
                sum += game_id

            power_sum += powerof_marbles(max_revealed)

    return sum, power_sum


def main(inputfile):
    part_one, part_two = parse_game(inputfile)
    return part_one, part_two