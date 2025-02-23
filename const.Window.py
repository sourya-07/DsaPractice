arr = [-1, 2, 3, 3, 4, 5, -1]
k = 4
n = len(arr)
l, r  = 0, k-1
s = 0
for i in range(k) :
    s += arr[i]
# print(s)
max_sum = s
while r < n -1 :
    s = s - arr[l]
    l+=1
    r+=1
    s = s + arr[r]
    
    # max_sum = max(max_sum, s)
    if s > max_sum : 
        max_sum = s
print(max_sum)
