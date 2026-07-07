class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        for i in range(1,len(nums)):
            prev = nums[i-1]
            prefix[i] = prefix[i-1]*prev
        
        for i in range(len(nums)-2, -1, -1):
            next = nums[i+1]
            suffix[i] = suffix[i+1]*next

        final = prefix
        for i in range(len(nums)):
            final[i] = final[i]*suffix[i]
        return final
        
        

        