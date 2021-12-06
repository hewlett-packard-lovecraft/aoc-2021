# 1. take input, split input by /n/n
# 2. 1st line is special, put into aray nums
# 3. spli rest of input into grids
# 4. go through num, check each grid for num
# 5. check for win condition
# 6. repeat step 4-5

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


if __name__ == '__main__':
    grids = []
    nums = []
    called_out = []

    for board in open('day4/input_test.txt').read().split('\n\n'):
        grid = []
        if ',' in board:
            nums = board.split(',')  # first line is special
        else:
            for line in board.splitlines():
                row = list(map(int, line.split()))
                grid.append(row)

        grids.append(grid)
    
    grids.pop(0)
    
    for i, num in enumerate(nums):
        called_out.append(num)
        for grid in grids:
            if has_won(grid, called_out):
                print(uncalled_numbers_sum(grid, called_out))
                break
