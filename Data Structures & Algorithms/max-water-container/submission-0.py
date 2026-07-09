class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maxArea = min(heights[0],heights[len(heights)-1]) * (len(heights)-1)
        while(left < right):
            currentArea = min(heights[left],heights[right]) * (right-left)
            if(currentArea > maxArea):
                maxArea = currentArea
            if(heights[left] < heights[right]):
                left += 1
            else:
                right -= 1
        return maxArea