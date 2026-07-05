class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in nums:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        
        frq = [[] for i in range(len(nums)+1)]
        for num, count in map.items():
            frq[count].append(num)
        
        results = []
        count = 0
        for i in reversed(frq):
            for j in i:
                results.append(j)
                if len(results) == k:
                    return results
                count+=1
        

            

