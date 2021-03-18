# Given an array of integers nums.
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# Return the number of good pairs.

# pretty sure this is the most efficient way to do it
# O(N) time
def numIdenticalPairs(nums: List[int]) -> int:
    frequency = {}
    for num in nums:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    goodPairs = 0
    for element in frequency:
        n = frequency[element]
        goodPairs += (n * (n - 1) // 2)
    return goodPairs

