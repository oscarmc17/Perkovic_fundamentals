# Recursion

def countdown(n):
    'counts down to 0'
    if n <= 0:  # base case
        print('Blastoff!!!')
    else:           # n > 0: recursive step
        print(n)        # print n first and then
        countdown(n-1)  # count down from n-1 to 0 recursively

print(countdown(3))

# function reversed()
def countdown(n):
    for i in reversed(range(n+1)):
        print(i)

print(countdown(3))

# function using just range()
def countdown(n):
    for i in range(n, -1, -1):  # start at 3, stop right before -1 (0), range decreases by -1.
        print(i)


print(countdown(3))
