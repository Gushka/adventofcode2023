import importlib.util
import sys
import os.path
import argparse
import time

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

def solve(day=None, testfile=None):
    if day:
        if len(str(day)) == 1:
            day = f"0{day}"
        module_name = f"day{str(day)}"
        testfile = os.path.join(module_name, testfile)
        module_path = os.path.join(CURRENT_DIR, os.path.join(module_name, f"{module_name}.py"))
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        return(module.main(testfile))

def print_all(inputfile):
    solved_days = []
    print("--- ADVENT OF CODE 2023 ---\n")
    for day in range(1, 26):
        day_number = day
        if len(str(day_number)) == 1:
            day_number = f"0{day_number}"
        day_path = os.path.join(CURRENT_DIR, os.path.normcase(f"day{day_number}"))

        results = []
        if p := os.path.exists(day_path):
            if f := os.path.isfile(os.path.join(day_path, f"day{day_number}.py")):
                start_time = time.time()
                results = solve(day, inputfile)
                elapsed = int((time.time() - start_time) * 1000)
                print(f"Day {day} results are:\n    Part one: {results[0]}\n    Part two: {results[1]}\n    took: {elapsed}ms\n")
                

def main():
    parser = argparse.ArgumentParser(description="Solve Advent of Code puzzle for a single day")
    parser.add_argument("day", nargs="?", help="day number of the desired puzzle, if omitted prints all", type=int)
    parser.add_argument("-t", help="test file name with extension. Default: input.txt",
                        type=str, default="input.txt")
    parser.add_argument("-i", "--instructions", help="print selected day's puzzle text with the objective",
                        action="store_true")

    args = parser.parse_args()

    if args.instructions:
        day_number = args.day
        if len(str(day_number)) == 1:
            day_number = f"0{day_number}"
        puzzle_text = os.path.join(CURRENT_DIR, os.path.join(f"day{day_number}", "puzzle.txt"))
        with open(puzzle_text, 'r') as file:
            for line in file:
                print(line)
    elif not args.day:
        print_all(args.t)
    else:
        start_time = time.time()
        results = solve(args.day, args.t)
        elapsed = int((time.time() - start_time) * 1000)
        print(f"Day {args.day} results are:\n    Part one: {results[0]}\n    Part two: {results[1]}\n    took: {elapsed}ms")

if __name__ == "__main__":
    main()
