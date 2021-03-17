# Naive approach that takes up a lot of space, and is very slow
# O(2^N) time | O(N) space
def getNthFibNaive(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFibNaive(n - 1) + getNthFibNaive(n - 2)

# same as the naive approach but reduces the time complexity
# by avoiding duplicate calculations, uses the same amount of space
# O(N) time | O(N) space
def getNthFibCache(n, cache = {1: 0, 2: 1}):
    if n in cache:
        return cache[n]
    else:
        n = getNthFibCache(n - 1, cache) + getNthFibCache(n - 2, cache)
        return cache[n]

# reduces space complexity significantly, as we are only storing 2 values in an array
# and manipulating the same array
# O(N) time | O(1) space
def getNthFibIter(n):
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
    return lastTwo[1] if n > 1 else lastTwo[0]

