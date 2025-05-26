# Q1. Create a recursion function to print n to 1 :-


# def print1(n) : 
#     if n == 5 :
#         print(5)
#         return
    
#     print1(n+1)    
#     print(n)
    
# print1(1)  


# def print1(n) : # by kunal khuswaha
#     if n == 0 :
#         return
    
#     print(n)
#     print1(n-1)    
    
# print1(5)  








# Q2. Create a recursion function to print 1 to n :-

# def fun(n) :
#     if n == 6 :
#         return
    
#     print(n)
#     fun(n+1)
    
    
# fun(1)



# def fun(n) : #By kunal khuswaha
#     if n == 0 :
#         return
    
#     fun(n-1)
#     print(n)
    
# fun(5)






# Q3. Factorial of a number :-

# def fact(n) :
#     if n == 0 :
#         return 1

#     else :
#         return (n * fact(n-1))
    
# print(fact(5))



# Q4. Sum of digits :-
# n = 1342   ans = 1+3+4+2 = 10


# def sum_digits(n) :
#     if n == 0 :
#         return 0
#     else :
#         temp = n % 10
#         return (temp + sum_digits(n // 10))

# print(sum_digits(1342))





# Q5. product of a number :-


# def product(n) :
#     if n % 10 == n :
#         return n
#     return (n%10 * product(n // 10))

# print(product(1324))






# Concept: Passing Numbers :-


# def Pass(n) :
#     if n == 0 :
#         return 
#     print(n)
#     Pass(n-1)
    
# (Pass(5))




# Q7. Reverse a Number :-


# Way 1.

# def reverse(n, sum = 0) :
#     if n == 0:
#         return sum
#     else :
#         rem = (n % 10) 
#         sum = sum * 10 + rem
#         return reverse(n // 10, sum)
    
# print(reverse(1342))

#  Way 2.

