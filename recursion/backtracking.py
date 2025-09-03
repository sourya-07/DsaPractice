def all_path(path, maze, r, c, step_matrix, step):
    if r == len(maze) - 1 and c == len(maze[0]) - 1:
        step_matrix[r][c] = step
        print(path)
        for row in step_matrix:
            print(row)
        print()
        return

    if not maze[r][c]:
        return

    maze[r][c] = False
    step_matrix[r][c] = step

    if r < len(maze) - 1:
        all_path(path + "D", maze, r + 1, c, step_matrix, step + 1)
    if r > 0:
        all_path(path + "U", maze, r - 1, c, step_matrix, step + 1)
    if c > 0:
        all_path(path + "L", maze, r, c - 1, step_matrix, step + 1)
    if c < len(maze[0]) - 1:
        all_path(path + "R", maze, r, c + 1, step_matrix, step + 1)

    maze[r][c] = True         # backtrack visited
    step_matrix[r][c] = 0     # backtrack steps

# Maze grid
board = [
    [True, True, True], 
    [True, True, True], 
    [True, True, True]
]

# Step tracking matrix
step_matrix = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

# Call the function
all_path('', board, 0, 0, step_matrix, 1)



















