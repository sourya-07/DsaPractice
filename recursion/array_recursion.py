# Q1. find if array is Sorted or not :-

# def check_sorted(arr) :
#     return helper(arr, 0)

# def helper(arr, i) :
#     if len(arr) - 1 == i :
#         return True
#     if arr[i] > arr[i+1] :
#         return False
    
#     return helper(arr, i + 1)
    
# print(check_sorted([1, 3, 5, 7, 8]))


# def check_sorted(arr, i = 0) : # without helper Function
#     if i == len(arr) - 1 :
#         return True
#     if arr[i] > arr[i + 1] :
#         return False
    
#     return check_sorted(arr, i + 1)
    
# print(check_sorted([1, 3, 5, 6, 7]))




# Q2. Linear Search :-


# def search(arr) :
#     return helper(arr, 0, 1)

# def helper(arr, i, tar) :
#     if len(arr) == i:
#         return -1
    
#     if arr[i] == tar :
#         return i 
    
#     return helper(arr, i + 1, tar)

# print(search([1, 4, 2, 6]))


def search(arr, tar, i = 0) :
    if len(arr) - 1 == i :
        return -1
    
    if arr[i] == tar :
        return i 
    
    return search(arr, tar, i + 1)

print(search([1, 3, 2, 5, 7], 3))