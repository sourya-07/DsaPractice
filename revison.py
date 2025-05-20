# # Prefix Sum 

# arr = [1, 2, 3, 4]

# prr = [0] * len(arr)
# prr[0] = arr[0]

# for i in range(1, len(arr)) :
#     prr[i] = prr[i-1] + arr[i]
    
# print(prr)


# Two pointer technique :-

# arr = [1, 2, 3, 4, 5]
# tar = 2

# l, r = 0, len(arr) - 1
# ans = False
# for i in range(len(arr)) :
#     if arr[l] + arr[r] == tar :
#         ans = True 
#     elif arr[l] + arr[r] < tar : 
#         l += 1
#     else :
#         r -= 1

# print(ans)






# Bubble sort :-

# arr = [5, 4, 3, 2, 1]

# for i in range(len(arr)-1, -1, -1) :
#     for j in range(i) :
#         if arr[j] > arr[j+1] :
#             arr[j], arr[j+1] = arr[j+1], arr[j]

# print(arr)



# selection sort :-

# arr = [5, 4, 3, 2, 1]

# for i in range(len(arr)) :
#     mini = i
#     for j in range(i+1, len(arr)) :
#         if arr[j] < arr[mini] :
#             mini = j
#     arr[i], arr[mini] = arr[mini], arr[i]

# print(arr)


# Insertion sort :-

# arr = [5, 4, 8, 3, 2, 10, 3, 1] 

# for i in range(1, len(arr)) :
#     key = arr[i]
#     j = i - 1
#     while j >= 0 and arr[j] > key :
#         arr[j+1] = arr[j]
#         j -= 1
#         arr[j+1] = key
# print(arr)






# def merge(arr1, arr2) :
#     p1 = p2 = 0
#     merge = []
    
#     while p1 < len(arr1) and p2 < len(arr2) :
#         if arr1[p1] < arr2[p2] :
#             merge.append(arr1[p1])
#             p1 += 1
#         else :
#             merge.append(arr2[p2])
#             p2 += 1
    
#     merge += arr1[p1:]
#     merge += arr2[p2:]
#     return merge




# def merge_sort(arr):
    
#     if len(arr) == 1 :
#         return arr 

#     mid = len(arr) // 2
    
#     first = merge_sort(arr[:mid])
#     second = merge_sort(arr[mid:])
    
#     return merge(first, second)
    
# arr = [5, 4, 3, 2, 1]  
# print(merge_sort(arr))




