# Q1. Create a recursion function to print n to 1 :-

# def print1(n) : # by kunal khuswaha
#     if n == 0 :
#         return
    
#     print(n)
#     print1(n-1)    
    
# print1(5)  








# Q2. Create a recursion function to print 1 to n :-

# def fun_rev(n) : #By kunal khuswaha
#     if n == 0 :
#         return
    
#     fun_rev(n-1)
#     print(n)
    
# fun_rev(5)






# Q3. Factorial of a number :-

# def factorial(n) :
#     if n == 0 :
#         return 1
    
#     return n * factorial(n-1)

# print(factorial(5))  # Output: 120



# Q4. Sum of digits :-
# n = 1342   ans = 1+3+4+2 = 10

# def sum_digit(n) :
#     if n == 0 :
#         return 0
    
#     return n % 10 + sum_digit(n // 10)
# print(sum_digit(1342))  # Output: 10




# Q5. product of a number :-


# def digit_product(n) :
#     if n == 0 :
#         return  1
    
#     return n % 10 * digit_product(n // 10)

# print(digit_product(234))




# Concept: Passing Numbers :-


# def Pass(n) :
#     if n == 0 :
#         return 
#     print(n)
#     Pass(n-1)
    
# (Pass(5))




# Q7. Reverse a Number :-


# def reverse_num(n, sum = 0) :
#     if n == 0 :
#         return sum 
    
#     rem = n % 10
#     sum = sum * 10 + rem
#     n //= 10
    
#     return reverse_num(n, sum)

# print(reverse_num(1342)) 








# Q8. Palindrome :-

# def reverse_num(n, sum = 0) :
#     if n == 0 :
#         return sum
    
#     rem = n % 10
#     sum = sum * 10  + rem
#     n //= 10
#     return reverse_num(n, sum)

# def palindrome(n) :
    
#     return reverse_num(n) == n
#     # if reverse_num(n) != n : # This is also correct
#     #     return False
    
#     # return True

# print(palindrome(121))







# Q9. Count Zeros :- 

# def count_zeros(n, c = 0) :
#     if n == 0 :
#         return c

#     rem = n % 10
#     if rem == 0 :
#         c += 1
    
#     return count_zeros(n // 10, c)

# print(count_zeros(230901))


# Using helper function


def count_zeros_helper(n, c):
    
    if n == 0 :
        return c
    
    rem = 0
    if rem == 0 :
        c += 1
    return count_zeros_helper(n // 10, c)


def count_zeros(n) :
    return count_zeros_helper(n, 0)

print(count_zeros(1909800))