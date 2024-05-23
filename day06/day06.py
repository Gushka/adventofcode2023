from functools import reduce

def is_valid_record(time_frame, record_distance, hold_time):
    if hold_time >= time_frame:
        return False
    race_time = time_frame - hold_time
    traveled_distance = race_time * hold_time
    if traveled_distance > record_distance:
        return True
    else:
        return False

def test_records(time_frame, record_distance):
    record_count = 0
    for hold_time in range(1, time_frame):
        if is_valid_record(time_frame, record_distance, hold_time):
            record_count += 1
    
    return record_count

def part_one(data):
    result = []
    for race in range(len(data[0])):
        time = int(data[0][race])
        dist = int(data[1][race])
        result.append(test_records(time, dist))

    return reduce(lambda x, y: x * y, result)

def part_two(data):
    data[0] = ''.join(data[0])
    data[1] = ''.join(data[1])

    return test_records(int(data[0]), int(data[1]))

def main(inputfile):
    data = []
    with open(inputfile, 'r') as file:
        for line in file:
            data.append([elem for elem in line.split(": ")[1:][0].strip().split(" ") if elem != ''])

    return part_one(data), part_two(data)
