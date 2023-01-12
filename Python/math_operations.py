def factorial(x):
    if x == 1:
        return x
    return x * factorial(x-1)


def combinatorics(n, r):
    return factorial(n)/(factorial(r)*factorial(n-r))

