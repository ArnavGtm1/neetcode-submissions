class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        result = [0]*len(temperatures)
        for i in range(len(temperatures)):
            if i > 0 and temperatures[i] > temperatures[i-1]:
                while stk and temperatures[stk[-1]] < temperatures[i]:
                    index = stk.pop()
                    result[index] = i-index
            stk.append(i)
        return result

