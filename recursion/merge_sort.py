# def mergeSort(arr):
#     if len(arr) > 1 :
#         left_arr = arr[:len(arr) // 2]
#         right_arr = arr[len(arr) // 2:]
        
#         # recursion
#         mergeSort(left_arr)
#         mergeSort(right_arr)
        
#         #  Merge
#         i = 0  # left array index
#         j = 0  # right array index
#         k = 0  # merged array index
        
#         while i < len(left_arr) and j < len(right_arr):
#             if left_arr[i] < right_arr[j] :
#                 arr[k] = left_arr[i]
#                 i += 1
#             else :
#                 arr[k] = right_arr[j]
#                 j += 1
                
#             k += 1
        
#         while i < len(left_arr) :
#             arr[k] = left_arr[i]
            
#             i += 1
#             k += 1
        
#         while j < len(right_arr) :
#             arr[k] = right_arr[j]
#             j += 1
#             k += 1
        
#     return arr       



# arr = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 9]
# print(mergeSort(arr))










def mergeSort(arr):
    if len(arr) > 1 :
        left_arr = arr[:len(arr) // 2]
        right_arr = arr[len(arr) // 2:]

        mergeSort(left_arr)
        mergeSort(right_arr)
        
        i = j = k = 0
        
        while i < len(left_arr) and j < len(right_arr) :
            if left_arr[i] < right_arr[j] :
                arr[k] = left_arr[i]
                i += 1
                k += 1
            
            else :
                arr[k] = right_arr[j]
                j += 1
                k += 1
        
        while i < len(left_arr) :
            arr[k] = left_arr[i]
            i += 1
            k += 1
            
        while j < len(right_arr) :
            arr[k] = right_arr[j]
            j += 1
            k += 1
            
    return arr



arr = [2, 3, 5, 1, 7, 4, 4, 4, 2, 6, 9]
print(mergeSort(arr))