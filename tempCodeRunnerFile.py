arr = [2, 4, 6, 8, 9, 34, 34, 36, 65]
target = 34
n = len(arr)
l, r = 0, n-1
while l < r :
    mid = (l + r) // 2
    if l > r :
        break
    if arr[mid] == target :
        print(mid)
        break
    elif arr[mid] < target :
        l = mid + 1
    else :
        r = mid - 1
else :
    print(-1)