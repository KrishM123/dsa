class Solution(object):
    def trap(self, height):
        tot = 0
        left = 1
        right = len(height) - 2
        max_left = height[0]
        max_right = height[right + 1]
        while left <= right:
            if max_left <= max_right:
                if (max_left - height[left] > 0):
                    tot += max_left - height[left]
                if height[left] > max_left:
                    max_left = height[left]
                left += 1
            else:
                if (max_right - height[right] > 0):
                    tot += max_right - height[right]
                if height[right] > max_right:
                    max_right = height[right]
                right -= 1

        return tot