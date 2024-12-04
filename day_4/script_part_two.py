def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])

    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    # Check if a given diagonal is MAS or SAM
    # center is 'A', we just need to ensure that on both ends of this diagonal
    # we have one 'M' and one 'S' in any order.
    def check_diagonal(r1, c1, r2, c2):
        if not (in_bounds(r1, c1) and in_bounds(r2, c2)):
            return False
        chars = {grid[r1][c1], grid[r2][c2]}
        return chars == {"M", "S"}  # Both must be present

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "A":
                # Check the two diagonals
                # "\ diagonal": top-left and bottom-right
                diag1 = check_diagonal(r - 1, c - 1, r + 1, c + 1)
                # "/ diagonal": top-right and bottom-left
                diag2 = check_diagonal(r - 1, c + 1, r + 1, c - 1)

                if diag1 and diag2:
                    count += 1
    return count


with open("./day_4/input.txt", "r") as file:
    content = file.read()
    grid_rows = content.split("\n")
    grid = [list(line) for line in grid_rows if line != ""]

    result = count_xmas(grid)
    print(f"Number of times occurrences: {result}")
