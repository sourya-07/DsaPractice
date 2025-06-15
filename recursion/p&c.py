# def permutations(p, up) :
#     if len(up) == 0 :
#         return [p]
    
#     ans = []
#     for i in range(len(up)):
#         ch = up[i]
#         ans += permutations(p + [ch], up[:i] + up[i+1:])
#     return ans
    
# print(permutations([], [1, 23]))



# def permutations(p, up) :
#     if len(up) == 0 :
#         return [p]
    
#     ans = []
#     for i in range(len(up)) :
#         ch = up[i]
#         first = p[:i]
#         second = p[i+1:]
#         ans += permutations(p + [ch], first + second)
    
#     return ans
    
    
# print(permutations([], [1, 23]))








# leetcode 17 :- Letter Combinations of a Phone Number

# def pad(p, up) :
#     if len(up) == 0 :
#         return [p]

#     digit = ord(up[0]) - ord("0")
#     mapping = ["", "", "abc", "def", 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', "wxyz"]
    
#     letters = mapping[digit]
    
#     res = []
#     for i in range(len(letters)) :
        
#         ch = letters[i]
#         recursive_call = pad(p + ch, up[1:])
#         for j in range(len(recursive_call)) :
#             res.append(recursive_call[j])
    
#     return res
        
# print(pad("", "23"))












# leetcode 1155 :- Number of Dice Rolls With Target Sum:


# def dice_rolls(p, target) :
#     if target == 0 :
#         return [p]
    
#     res = []
#     for i in range(1, 7) :
#         if i <= target :
#             call = dice_rolls(p + [i], target - i)
#             for j in range(len(call)) :
#                 res.append(call[j])
                
#     return res

# print(dice_rolls([], 3))