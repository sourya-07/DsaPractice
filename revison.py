# Prefix Sum 

arr = [1, 2, 3, 4]

prr = [0] * len(arr)
prr[0] = arr[0]

for i in range(1, len(arr)) :
    prr[i] = prr[i-1] + arr[i]
    
print(prr)