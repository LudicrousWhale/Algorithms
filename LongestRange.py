def findLongestRange(array):
    bestRange = []
    longestLength = 0
    explored = {}
    for num in array:
        explored[num] = True
    for num in array:
        if not explored[num]:
            continue
        explored[num] = False
        currentLength = 1
        left = num - 1
        right = num + 1
        while left in explored:
            explored[left] = False
            currentLength += 1
            left -= 1
        while right in explored:
            explored[right] = False
            currentLength += 1
            right += 1
        if currentLength > longestLength:
            longestLength = currentLength
            bestRange = [left + 1, right - 1]
    return bestRange

# driver code
array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
print(findLongestRange(array))