#original fibonacchi
def fib1(n):
    if n <= 2:
        return 1
    return fib1(n - 1) + fib1(n - 2)

print(fib1(6))

#memoized fibonacci
def fib(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

print(fib(6))