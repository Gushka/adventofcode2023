def main(inputfile):
    with open(inputfile, 'r') as file:
        instr, nodes = file.split("\n\n")
        print(instr, nodes)
    return None, None