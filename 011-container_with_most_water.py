class Solution:
    def maxArea(self, height) -> int:
        if (len(height) == 1) : return 0
        if (len(height) == 2) : return min(height[0], height[1])

        left = 0
        right = len(height) - 1
        max_area = 0

        #O(n) (?)
        while (left != right):
            area = min(height[left],height[right])*(right-left)
            if (area > max_area):
                max_area = area
            if (height[left] <= height[right]):
                left = left + 1
            else:
                right = right - 1

        return max_area
