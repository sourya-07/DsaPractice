
s = ['h', 'e', 'l', 'l', 'o']

n = len(s)
for i in range(n//2):
    temp = s[i]
    s[i] = s[n-1-i]
    s[n-1-i] = temp
    