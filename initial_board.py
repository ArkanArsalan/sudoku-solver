import sys
import argparse

def parse_argument():
    parser = argparse.ArgumentParser(description="Sudoku solver")
    
    parser.add_argument("-f", "--file", help="Initial board file .txt", type=str, required=True)

    arguments = parser.parse_args()

    return arguments

def open_file():
    board = []

    filename = parse_argument().file

    file_path = f"./initial_board/{filename}"
    with open(file_path, "r") as file:
        lines = file.readlines()

        for line in lines:
            line = line.replace("\n", "")
            numbers = [int(num) for num in line.split()]
            board.append(numbers)

    return board