# Given n non-negative integers a1, a2, ..., an , where each represents a 
# point at coordinate (i, ai). n vertical lines are drawn such that the two 
# endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, 
# together with the x-axis forms a container, such that the container contains 
# the most water.
# Notice that you may not slant the container.

def maxArea(height):
    max_so_far = 0
    i = 0
    j = len(height) -1
    y_axis = 0
    while i < j:
        if height[i] < height[j]:
            y_axis = height[i]
        else:
            y_axis = height[j]
        max_area = y_axis*(j-(i))
        max_so_far = max(max_area, max_so_far)
        if height[i] < height[j]:
            i += 1
        elif height[i] > height[j]:
            j -= 1
        else:
            i += 1
            j -= 1
    return max_so_far

# driver code
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
