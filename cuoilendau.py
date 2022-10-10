from functools import lru_cache


@lru_cache
def fib(n):
    print(f'Calculate the Fibonacci of {n}')
    if n < 2:
        return 1
    return fib(n-2) + fib(n-1)


fib(6)