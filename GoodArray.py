import math

def isGoodArray(nums):
    # we just have to check if gcd(subset of nums) == 1
    # python one liner
    return math.gcd(*nums) == 1

# driver code
nums = [12,5,7,23]
print(isGoodArray(nums))