# Count patterns :-

# def count_path(r, c) :
#     if r == 1 or c == 1 :
#         return 1
    
#     left = count_path(r - 1, c)
#     right = count_path(r, c - 1)
    
#     return left + right


# print(count_path(3, 3))




# Printing Paths :-

# def print_path(path, r, c) :
#     if r == 1 and c == 1 :

#         return [path]
#     left, right = [], []
#     if r > 1 :
#         left = print_path(path + ["D"],r - 1, c)
    
#     if c > 1 :
#         right = print_path(path + ['R'],r, c - 1)
        
#     return left + right

# print(print_path([], 3, 3))






# Including Diagonal Paths :-


# def diagonal_paths(path, r, c) :
    # if r == 1 and c == 1 :
    #     return [path]
    
    # left, right , diagonal = [], [], []
    
    # if r > 1 and c > 1 :
    #     diagonal = diagonal_paths(path + ['D'], r -1, c - 1)
        
    # if r > 1 :
    #     left = diagonal_paths(path + ['H'], r - 1, c)
    
    
    # if c > 1 :
    #     right = diagonal_paths(path + ['V'], r, c - 1)
        
#     return diagonal + left + right


# print(diagonal_paths([], 3, 3))






# Maze with obstacles :-

def maze_obstacles(path, maze, r, c) :
    if r == len(maze) and len(maze) == 1 :
        return [path]
    
    left, right , diagonal = [], [], []
    
        
    if r > 1 :
        left = maze_obstacles(path + ['H'],maze, r - 1, c)


    if c > 1 :
        right = maze_obstacles(path + ['D'],maze, r, c - 1)
        
    