from pathlib import Path
from collections import Counter


# 1. split input into array of x_1 y_1 x_2 y_2
# 2. remove diagonals
# 3. expand ranges
# 4. count duplicates``


def coords_in_range(x_1, y_1, x_2, y_2):
    coords = []

    for x in range(min(x_1, x_2), max(x_1, x_2)+1):
        for y in range(min(y_1, y_2), max(y_1, y_2)+1):
            coords.append([x, y])

    return(coords)


def count_dup(grid):
    a = dict(Counter(map(tuple, grid)))

    counter = 0
    for v in a.values():
        if v > 1:
            counter += 1
   
    return counter


def task_1(data):
    grid = []

    for line in data:
        x_1, y_1 = map(int, line[0].split(','))
        x_2, y_2 = map(int, line[1].split(','))

        if(x_1 == x_2 or y_1 == y_2):
            grid += coords_in_range(x_1, y_1, x_2, y_2)

    print(count_dup(grid))
            

def task_2(data):
    grid = []

    for line in data:
        x_1, y_1 = map(int, line[0].split(','))
        x_2, y_2 = map(int, line[1].split(','))

        if x_1 == x_2 or y_1 == y_2:
            grid += coords_in_range(x_1, y_1, x_2, y_2)

        elif abs(x_2 - x_1) == abs(y_2 - y_1):
            grid += coords_in_range(x_1, y_1, x_2, y_2)

    print(count_dup(grid))


if __name__ == '__main__':
    data = []
   
    with open(Path('day5/input_test.txt'), encoding='utf-8', mode='r') as f:
        for line in f:
            data.append(line.split('->'))

    task_1(data)
    task_2(data)
