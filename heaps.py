arr = [10, 7, 6, 4, 5, 4, 5, 3, 2]
def heapifyDown(arr, ind):
    n = len(arr)
    largest_ind = ind
    
    left_child_ind = 2 * ind + 1
    right_child_ind = 2 * ind + 2
    
    if left_child_ind < n and arr[left_child_ind] > arr[largest_ind]:
        largest_ind = left_child_ind
    
    if right_child_ind < n and arr[right_child_ind] > arr[largest_ind]:
        largest_ind = right_child_ind
    
    if largest_ind != ind:
        arr[largest_ind], arr[ind] = arr[ind], arr[largest_ind]
        heapifyDown(arr, largest_ind)
    return arr    

heapifyDown(arr, 3)