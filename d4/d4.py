def check_neighbours(row, col, grid):
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if (
                col + dc < 0
                or row + dr < 0
                or row + dr >= len(grid)
                or col + dc >= len(grid[0])
                or (dr == 0 and dc == 0)
            ):
                continue
            elif grid[row + dr][col + dc] == '@':
                count += 1
    return count


def part1():
    print('----part one----')
    with open('hint1.txt') as f:
        lines = 'not empty'
        grid = []
        while lines:
            lines = f.readline().strip()
            if lines:
                grid.append([x for x in lines])

    copy_grid = [row[:] for row in grid]
    rolls = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '@' and check_neighbours(row, col, grid) < 4:
                rolls += 1
                copy_grid[row][col] = 'x'
    print(f'Total rolls: {rolls}')
    print('Final grid:')
    for row in copy_grid:
        print(''.join(row))




# part1()
def part2():
    print('----part two----')

    with open('hint1.txt') as f:
        lines = 'not empty'
        grid = []
        while lines:
            lines = f.readline().strip()
            if lines:
                grid.append([x for x in lines])

    copy_grid = [row[:] for row in grid]
    total_rolls = 0
    while True:
        start_rolls = total_rolls
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '@' and check_neighbours(row, col, grid) < 4:
                    total_rolls += 1
                    copy_grid[row][col] = 'x'
        if start_rolls == total_rolls:
            break
        grid = [row[:] for row in copy_grid]
    print(f'Total rolls: {total_rolls}')
    print('Final grid:')
    for row in copy_grid:
        print(''.join(row))
part2()
