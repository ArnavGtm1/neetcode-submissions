class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maxArea = 0
        while(left < right):
            currentArea = (heights[left] if heights[left] < heights[right] else heights[right]) * (right - left)
            if(currentArea > maxArea):
                maxArea = currentArea
            if(heights[left] < heights[right]):
                left += 1
            else:
                right -= 1
        return maxArea