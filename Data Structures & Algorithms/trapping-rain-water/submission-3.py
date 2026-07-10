class Solution:
    def trap(self, height: List[int]) -> int:
        #The two-pointer algorithm calculates trapped water in O(1) space by starting pointers at both ends of the elevation map and moving the pointer bounded by the smaller maximum height inward. 
        #This ensures that the water trapped at each step is accurately calculated against its true limiting bottleneck on the fly, eliminating the need to store boundary heights in extra arrays.
        left = 0
        right = len(height)-1
        leftMax = height[left]
        rightMax = height[right]
        total = 0
        while(left < right):
            if(leftMax < rightMax):
                left += 1
                if(height[left] > leftMax):
                    leftMax = height[left]
                total += leftMax - height[left]
            else:
                right -= 1
                if(height[right] > rightMax):
                    rightMax = height[right]
                total += rightMax - height[right]
            
        return total

                







                


        