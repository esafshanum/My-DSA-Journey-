class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        ans = 0

        while left < right:
            h = min(height[left], height[right])
            ans = max(ans, h * (right - left))

            if height[left] < height[right]:
                curr = height[left]
                while left < right and height[left] <= curr:
                    left += 1
            else:
                curr = height[right]
                while left < right and height[right] <= curr:
                    right -= 1

        return ans