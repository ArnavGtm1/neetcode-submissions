class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        for s in strs:
            counts = [0]*26
            for i in s:
                index = ord(i)-ord('a')
                counts[index] += 1
            result = tuple(counts)
            if result in store:
                store[result].append(s)
            else:
                store[result] = [s]
        
        return list(store.values())
