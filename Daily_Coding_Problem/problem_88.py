#[MEDIUM][SOLVED] Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.


def divide(num1, num2):
    quotient = 0

    while num1 >= num2:
        num1 -= num2
        quotient += 1
    
    return quotient

print("15/5 = 3 ", divide(15,5))
print("25/5 = 5 ",divide(25,5))
print("5/2 = 2 ",divide(5,2))
print("7/3 = 2 ",divide(7,3))
print("34/8 = 4 ",divide(34,8))