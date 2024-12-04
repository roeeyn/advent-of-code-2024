def count_occurrences(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    directions = [
        (-1, 0),  # up
        (1, 0),  # down
        (0, -1),  # left
        (0, 1),  # right
        (-1, -1),  # up-left diagonal
        (-1, 1),  # up-right diagonal
        (1, -1),  # down-left diagonal
        (1, 1),  # down-right diagonal
    ]

    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def check_direction(r, c, dr, dc):
        """Check if the word can be found starting at (r, c) in direction (dr, dc)."""
        for i in range(word_length):
            nr, nc = r + dr * i, c + dc * i
            if not in_bounds(nr, nc) or grid[nr][nc] != word[i]:
                return False
        return True

    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == word[0]:  # Only start checking if first letter matches
                for dr, dc in directions:
                    if check_direction(r, c, dr, dc):
                        count += 1
    return count


with open("./day_4/input.txt", "r") as file:
    content = file.read()
    grid_rows = content.split("\n")
    grid = [list(line) for line in grid_rows if line != ""]

    word = "XMAS"
    result = count_occurrences(grid, word)
    print(f"Number of times {word} appears: {result}")


# # Example usage:
# grid = [
#     "MMMSXXMASM",
#     "MSAMXMSMSA",
#     "AMXSXMAAMM",
#     "MSAMASMSMX",
#     "XMASAMXAMM",
#     "XXAMMXXAMA",
#     "SMSMSASXSS",
#     "SAXAMASAAA",
#     "MAMMMXMMMM",
#     "MXMXAXMASX",
# ]

# Convert each string to a list of characters (optional, but often convenient)
# grid = [list(row) for row in grid]

# word = "XMAS"
# result = count_occurrences(grid, word)
# print(f"Number of times {word} appears: {result}")
