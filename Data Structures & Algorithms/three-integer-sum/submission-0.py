class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final = []
        for i in range(len(nums)):
            if(i>0 and nums[i] == nums[i-1]):
                continue
            target = -nums[i]
            left = i+1
            right = len(nums)-1
            while(right > left):
                if(nums[left] + nums[right] == target):
                    result = [nums[i], nums[left], nums[right]]
                    final.append(result)
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif(nums[left] + nums[right] > target):
                    right = right -1
                elif(nums[left] + nums[right] < target):
                    left = left + 1
        return final


                    


