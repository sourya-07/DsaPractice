
def all_path(paths, maze, r, c) :
    if r == len(maze) - 1 and len(maze[0]) - 1 == c :
        return [paths]
    
    if not maze[r][c]:
        return []
    
    maze[r][c] = False
    
    down, right, left, up = [], [], [], []
    
    if r < len(maze) - 1 :
        down = all_path(paths + "D", maze, r + 1, c)
        
    if r > 0 :
        up = all_path(paths + "U", maze, r - 1, c)
    
    if c > 0 :
        left = all_path(paths + 'L', maze, r, c - 1)
    
    if c < len(maze[0]) - 1 :
        right = all_path(paths + 'R', maze, r, c + 1)
        
    return down + up + left + right

    maze[r][c] = True

board = [
    [True, True, True], 
    [True, True, True], 
    [True, True, True]
    ]

print(all_path('', board, 0, 0))



