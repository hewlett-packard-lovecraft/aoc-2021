from pathlib import Path

# 1. split input into array of x1 y1 x2 y2
# 2. remove diagonals
# 3. expand ranges
# 4. count duplicates``


def coords_in_range(x1, y1, x2, y2):
    coords = []

    #print(x1, y1, x2, y2)

    for x in range(min(x1, x2), max(x1, x2)+1):
        for y in range(min(y1, y2), max(y1, y2)+1):
            coords.append([x, y])

    #print(coords)

    return(coords)


def count_duplicates(grid):
    seen = set()
    counter = 0
    for n in grid:
        if tuple(n) in seen:
            print('duplicate:', n)
            counter += 1
        else:
            seen.add(tuple(n))  

    return counter

def task_1(data):
    grid = []

    for line in data:
        x1, y1 = map(int, line[0].split(','))
        x2, y2 = map(int, line[1].split(','))

        if(x1 == x2 or y1 == y2):
            grid += coords_in_range(x1, y1, x2, y2)

    print(count_duplicates(grid))
            

if __name__ == '__main__':
    data = []
   
    with open(Path('day5/input_test.txt'), encoding='utf-8', mode='r') as f:
        for line in f:
            data.append(line.split('->'))

    task_1(data)
