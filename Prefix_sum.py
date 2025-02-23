# # For given range this will work.

# lst = list(map(int, input().split()))

# prefix=[lst[0]]
# # print(prefix)
# s=lst[0]
# # print(s)
# for i in range(1,len(lst)):
#     s+=lst[i]
#     prefix.append(s)
# # print(prefix)


# n=int(input())
# for i in range(n):
#     l,r=map(int,input().split())
#     print(prefix[r]-prefix[l-1])


# One more approach:


arr = list(map(int, input().split()))

prefix = [0] * len(arr) 
prefix[0] = arr[0]  

for i in range(1, len(arr)):
    prefix[i] = prefix[i - 1] + arr[i]  

n = int(input())
for i in range(n):
    l, r = map(int, input().split())
    if l == 0:
        print(prefix[r])  
    else:
        print(prefix[r] - prefix[l - 1])  
