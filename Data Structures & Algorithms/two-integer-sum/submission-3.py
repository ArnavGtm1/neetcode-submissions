class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            current = nums[i]
            diff = target - current
            if current in seen:
                return [seen[current], i]
            seen[diff] = i
        return []

            