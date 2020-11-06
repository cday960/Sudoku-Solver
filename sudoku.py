import numpy as np


def main():
    width, height, puzzle = getPuzzle()
    solve(width, height, puzzle)


def getPuzzle():
    result = []
    height = int(input("How many rows: "))
    for y in range(height):
        row = [int(x) for x in input("Enter numbers separated by commas: ").split(',')]
        result.append(row)
    width = len(result[0])
    return width, height, result


def possible(puzzle, x, width, y, height, n):
    for i in range(0, width):
        if puzzle[y][i] == n:
            return False
    for i in range(0, height):
        if puzzle[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if puzzle[y0 + i][x0 + j] == n:
                return False
    return True


def solve(width, height, puzzle):
    for y in range(height):
        for x in range(width):
            if puzzle[y][x] == 0:
                for n in range(1, 10):
                    if possible(puzzle, x, width, y, height, n):
                        puzzle[y][x] = n
                        solve(width, height, puzzle)
                        puzzle[y][x] = 0
                return
    print(np.array(puzzle))
    input("Done")


main()
