# Chapter 10.1 - Recursion

# def countdown(n):
#     'counts down to 0'
#     if n <= 0:  # base case
#         print('Blastoff!!!')
#     else:           # n > 0: recursive step
#         print(n)        # print n first and then
#         countdown(n-1)  # count down from n-1 to 0 recursively

# print(countdown(3))

# # function reversed()
# def countdown(n):
#     for i in reversed(range(n+1)):
#         print(i)

# print(countdown(3))

# # function using just range()
# def countdown(n):
#     for i in range(n, -1, -1):  # start at 3, stop right before -1 (0), range decreases by -1.
#         print(i)


# print(countdown(3))


# def vertical(n):
#     'prints digits of n vertically'
#     if n < 10:      # base case: n has 1 digit
#         print(n)    # just print n
#     else:           # recursive step: n has 2 or more digits
#         vertical(n//10)     # recursively print all but last digit
#         print(n % 10)         # print last digits of n

# vertical(3124)


# Practice Problem 10.1
# def reverse(n):
#     'prints digits of n vertically'
#     if n < 10:      # base case: n has 1 digit
#         print(n)    # just print n
#     else:           # recursive step: n has 2 or more digits
#         print(n % 10)         # print last digits of n
#         reverse(n//10)     # recursively print all but last digit


# reverse(3124)


# Practice Problem 10.2
# def cheers(n):
#     'counts down to 0'
#     if n == 0:  # base case
#         print('Hurray!!!')
#     else:           # n > 0: recursive step
#         print('Hip', end=' ')        # print n first and then
#         cheers(n-1)  # count down from n-1 to 0 recursively

# print(cheers(5))


# Practice Problem 10.3
# def factorial(n):
#     'returns n!'
#     if n == 0:  # base case
#         return 1
#     return factorial(n-1) * n   # recursive step when n > 0

# print(factorial(10))

# ------------------------------- 10.4 -------------------------------
# def pattern(n):
#     'prints the nth pattern'
#     if n == 0:               # base case
#         print(0, end=" ")
#     else:                    # recursive step: n > 0
#         pattern(n-1)            # print n-1st pattern
#         print(n, end=" ")                # print n
#         pattern(n-1)            # print n-1st pattern

# pattern(1)

# PRACTICE PROBLEM 10.4
# def pattern2(n):
#     if n > 0:
#         pattern2(n-1)
#         print(n * '*')
#         pattern2(n-1)

# pattern2(0)
# pattern2(1)
# pattern2(2)
# pattern2(3)

# ------------------------------- 10.5 -------------------------------
# from turtle import Screen, Turtle


# def koch(n):
#     if n == 0:
#         return 'F'
#     tmp = koch(n-1)
#     return tmp+'L'+tmp+'R'+tmp+'L'+tmp

# def drawKoch(n):
#     'draws nth Koch curve using instructions from function koch()'
#     s = Screen()
#     t = Turtle()
#     directions = koch(n)

#     for move in directions:
#         if move == 'F':
#             t.forward(300/3**n)
#         if move == 'L':
#             t.lt(60)
#         if move == 'R':
#             t.rt(120)
#     s.bye()

# # koch(0)


# PRACTICE PROBLEM 10.5
# def drawSnowflake(n):
#     s = Screen()
#     t = Turtle()
#     directions = koch(n)

#     for i in range(3):
#         for move in directions:
#             if move == 'F':
#                 t.fd(300/3**n)
#             if move == 'L':
#                 t.lt(60)
#             if move == 'R':
#                 t.rt(120)
#                 t.rt(120)
#         s.bye()


# ------------------------------- 10.6 -------------------------------
# def recSum(lst):
#     'returns the sum of items in list lst'
#     if len(lst) == 0:
#         return 0
#     return recSum(lst[:-1]) + lst[-1]


# PRACTICE PROBLEM 10.6
# def recNeg(lst):
#     if len(lst) == 0:
#         return False
#     return recNeg(lst[:-1]) or lst[-1] < 0

# print(recNeg([3, 1, -1, 5]))
# print(recNeg([3, 1, 0, 5]))

# def recIncr(lst):
#     if len(lst) == 0:
#         return []
#     return recIncr(lst[:-1]) + [lst[-1]+1]

# lst = [1, 4, 9, 16, 25]
# # print(recIncr(lst))

# def f(i):
#     return i + 1

# def recMap(lst, f):
#     if len(lst) == 0:
#         return []
#     return recMap(lst[:-1], f) + [f(lst[-1])]


# print(recMap(lst, f))

def power(a, n):
    'returns a to the nth power'
    res = 1
    for i in range(n):
        res *= a
    return res

def rpower(a, n):
    if n == 0:
        return 1
    
    tmp = rpower(a, n//2)

    if n % 2 == 0:
        return tmp * tmp
    else:
        return a * tmp * tmp
