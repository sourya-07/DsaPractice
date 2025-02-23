lst = list(map(int, input().split()))

suff = [lst[-1]]*len(lst)
print(suff)


Sum = lst[-1]
# print(Sum)
for i in range(len(lst)-2, -1, -1):
    Sum += lst[i]
    # print(Sum)
    suff[i] = Sum

print(suff)