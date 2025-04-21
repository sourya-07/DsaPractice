def binary_search(arr, s, e, target):
    if s > e:
        return -1  # Element not found

    mid = (s + e) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, s, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, e, target)

arr = list(map(int, input().split()))
target = int(input())

result = binary_search(arr, 0, len(arr) - 1, target)

print(result if result != -1 else "Element not found")
