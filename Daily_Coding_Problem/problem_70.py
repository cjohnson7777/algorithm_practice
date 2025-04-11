#[EASY] A number is considered perfect if its digits sum up to exactly 10.

# Given a positive integer n, return the n-th perfect number.

# For example, given 1, you should return 19. Given 2, you should return 28.

def nth_perfect_number(n):
    num = 19
    i = 1

    while i < n:
        num += 9
        i += 1
    
    return num



print(nth_perfect_number(1))
print(nth_perfect_number(2))
print(nth_perfect_number(3))
print(nth_perfect_number(4))
print(nth_perfect_number(5))
print(nth_perfect_number(6))