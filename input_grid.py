def count_adjacent_mines(grid, row, col):
    """
    Count the number of mines adjacent to a specific cell in the grid.
    """
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # NW, N, NE
        (0, -1),         (0, 1),     # W,    E
        (1, -1), (1, 0), (1, 1)      # SW, S, SE
    ]
    count = 0
    rows, cols = len(grid), len(grid[0])
    
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '#':
            count += 1
    
    return count


def minesweeper(grid):
    """
    Replace each '-' in the grid with the number of adjacent mines.
    """
    rows, cols = len(grid), len(grid[0])
    result = [[cell for cell in row] for row in grid]  # Copy the grid
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '-':
                result[row][col] = str(count_adjacent_mines(grid, row, col))
    
    return result


# Example Input
input_grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

# Expected Output
output_grid = minesweeper(input_grid)

# Print the Result
for row in output_grid:
    print(" ".join(row))
