class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for i in nums:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1

        minheap = []
        for num, freq in map.items():
            heapq.heappush(minheap, (freq, num))
            if len(minheap)> k:
                heapq.heappop(minheap)

        result = []
        for (i,j) in minheap:
            result.append(j)

        return result
