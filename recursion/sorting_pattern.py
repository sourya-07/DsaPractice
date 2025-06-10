
# Q1. 
# * * * * *
# * * * *
# * * * 
# * *
# *


# def triangle(n) :
#     if n == 0 :
#         return ""
    
#     return ("* " * n) + "\n" + triangle(n - 1)
    

# print(triangle(5))



# Q2.
# *  
# * * 
# * * * 
# * * * * 
# * * * * *


# def triangle(n) :
#     if n == 0 :
#         return ""
    
#     return triangle(n - 1) + "\n" + ("* " * n)

# print(triangle(5))








# Bubble Sort :-

def bubble_sort(arr, r, c) :
    if r == 0 :
        return arr
    if c < r :
        if arr[c] > arr[c + 1] :
            arr[c], arr[c + 1] = arr[c + 1], arr[c]
        return bubble_sort(arr, r, c + 1)
        
    
    return bubble_sort(arr, r - 1, 0)
    
    return arr

arr = [2, 3, 1, 5, 4, 9, 7]
print(bubble_sort(arr, len(arr) - 1, 0))
