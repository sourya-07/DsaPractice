# arr = [2, 4, 6, 8, 9, 34, 34, 36, 65]
# target = 34
# n = len(arr)
# l, r = 0, n-1
# while l < r :
#     mid = (l + r) // 2
#     if l > r :
#         break
#     if arr[mid] == target :
#         print(mid)
#         break
#     elif arr[mid] < target :
#         l = mid + 1
#     else :
#         r = mid - 1
# else :
#     print(-1)





# For order agnostic Binary Search :-

# arr = [34, 25, 13, 10, 5 , 3, 2 ,1 ] 
# target = 5
# left, right = 0, len(arr) - 1
# is_ascending = arr[left] < arr[right]

# while left <= right:
#     mid = left + (right - left) // 2
    
#     if arr[mid] == target:
#         print(mid)
#         break
    
#     if is_ascending:
#         if target < arr[mid]:
#             right = mid - 1
#         else:
#             left = mid + 1
#     else:
#         if target > arr[mid]:
#             right = mid - 1
#         else:
#             left = mid + 1
# else:
#     print(-1)






# Ceiling of a number in a sorted array :- 


# arr = [2, 3, 5, 9, 14, 16, 18]
# t = int(input())

# l , r = 0, len(arr) - 1
# while l <= r:
#     mid = l + (r - l) // 2
#     if arr[mid] == t:
#         print(arr[mid])
#         break
    
#     elif arr[mid] < t:
#         l = mid + 1
        
#     else: 
#         ceiling = arr[mid]
#         r = mid - 1
        
# if ceiling != 1 :
#     print(ceiling)
# else :
#     print(-1)







# Floor of a Number :-

# arr = [2, 3, 5, 9, 14, 16]
# t = int(input())

# l , r = 0, len(arr) - 1
# while l <= r:
#     mid = l + (r - l) // 2
#     if arr[mid] == t:
#         print(arr[mid])
#         break
#     elif arr[mid] < t:
#         floor = arr[mid]
#         l = mid + 1
#     else:
#         r = mid - 1

# if floor != 1:
#     print(floor)
# else:
#     print(-1)







