class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        #Make seen set for o(1) lookups
        seen = set()
        for i in nums:
            seen.add(i)
        
        #Find sequence starters (if num-1 not in the list)
        seqStarters = []
        for num in nums:
            if num-1 not in seen:
                seqStarters.append(num)
        
        #Find the longest sequence
        maxCount = 1
        for i in seqStarters:
            count = 1
            current = i+1
            while(current in seen):
                count = count + 1
                current = current+1
            if count > maxCount:
                maxCount = count

        return maxCount



        