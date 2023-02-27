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
def factorial(n):
    'returns n!'
    if n == 0:  # base case
        return 1
    return factorial(n-1) * n   # recursive step when n > 0

print(factorial(10))