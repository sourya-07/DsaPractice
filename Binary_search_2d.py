





# def search(arr, target) :
    
#     r, c = 0, len(arr[0]) - 1
    
#     while r < len(arr) and c >= 0 :
        
#         if arr[r][c] == target :
#             return (r, c)
#         if arr[r][c] < target :
#             r += 1
#         else :
#             c -= 1
#     return -1


# arr = [[1, 2, 3, 4],
#        [5, 6, 7, 8],
#        [9, 10, 11, 12],
#        [13, 14, 15, 16]]
# target = 11

# print(search(arr, target))


# time complexity = O(n + m) where n is the number of rows and m is the number of columns









# Binary search in a 2D array or matrix :-


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
target = 11

rows, col = len(matrix), len(matrix[0])

top, bottom = 0, rows - 1

while top <= bottom :
    row_mid = (top + bottom) // 2
    
    if target > matrix[row_mid][len(matrix[0]) - 1] :
        top = row_mid + 1
    
    elif target < matrix[row_mid][0] :
        bottom = row_mid - 1
    
    else :
        break
    
if top > bottom :
    print("False")
    exit()

row = (top + bottom) // 2
left, right = 0, len(matrix[0]) - 1

while left <= right :
    mid = (left + right) // 2
    
    if matrix[row][mid] == target :
        print("True")
        break
    elif matrix[row][mid] < target :
        left = mid + 1
    elif matrix[row][mid] > target :
        right = mid - 1
else :
    print("False")