class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            current = nums[i]
            diff = target - current
            if current in dict:
                return [dict[current], i]
            dict[diff] = i
        return []

            