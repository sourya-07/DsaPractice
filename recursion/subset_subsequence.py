# String basic question :

# def remove_str(s, i = 0) :
#     if i == len(s) - 1:
#         return ""
#     if s[i] == 'a' :
#         return remove_str(s, i + 1)
#     else :
#         return s[i] + remove_str(s, i + 1)
         
# s = 'anceaade'
# print(remove_str(s))









# Subset and subsequence question patterns:

# used for questions like:- p&c, subsets => Non - adjacent collection.


# def subseq(p, up):
#     if up == "" :
#         return [p]

#     ch = up[0]

#     left = subseq(p + ch, up[1:])
#     right = subseq(p, up[1:])
    
#     return left + right

# print(subseq("", 'abc'))






# subsequence of a string with duplicates element :-



def subseq(p, up):
    up.sort()
    if len(up) == 0:
        return [p]
    
    ch = up[0]

    left = subseq(p + [ch], up[1:])
    right = subseq(p, up[1:])
    
    return left + right

print(subseq([], [1, 2, 2]))