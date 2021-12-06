def has_won(grid, called_out: list[int]):
    for row in grid:  # check rows
        if all(x in called_out for x in row):
            return True  # return true if all nums in row have been called out

    for row_index in range(len(grid[0])):
        if all(x[row_index] in called_out for x in grid):
            return True  # return true if all nums in col have been called out


def uncalled_numbers_sum(grid, called_out):
    all_nums = set()
    for row in grid:
        for x in row:
            all_nums.add(x)
    
    return sum(all_nums - set(called_out))

def task_1(grids, nums):
    for i, num in enumerate(nums):
        called_out.append(num)
        win = False

        for grid in grids:
            if has_won(grid, called_out):
                print('p1:', uncalled_numbers_sum(grid, called_out) * called_out[-1])
                win = True
                break
        
        if win:
            break

def task_2(grids, nums):
    final_score = 0
    for i, num in enumerate(nums):
        called_out.append(num)
        for grid in grids:
            if has_won(grid, called_out):
                final_score = uncalled_numbers_sum(grid, called_out) * called_out[-1]
                grids.remove(grid)
                break

    print('p2', final_score)
        


if __name__ == '__main__':
    grids = []
    nums = []
    called_out = []

    for board in open('day4/input_test.txt').read().split('\n\n'):
        grid = []
        if ',' in board:
            nums = map(int, board.split(','))  # first line is special
        else:
            for line in board.splitlines():
                row = list(map(int, line.split()))
                grid.append(row)

        grids.append(grid)
    
    grids.pop(0)
    
    task_1(grids, nums)
    task_2(grids, nums)