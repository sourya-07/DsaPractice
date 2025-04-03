arr= [1, 5, 3, 10, 9, 7]

for i in range(len(arr)) :
    j = i
    while j > 0 and arr[j-1] > arr[j] :
        arr[j-1], arr[j] = arr[j], arr[j-1]
print(arr)