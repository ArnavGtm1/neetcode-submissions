class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        store = []
        for i in range(len(position)):
            time = (target-position[i])/speed[i]
            store.append((position[i], time))
        store.sort(reverse = True)
        print(store)
        stk = [store[0]]
        for i in range(len(store)):
            if i == 0:
                continue
            data = store[i]
            time = data[1]
            if time > stk[-1][1]:
                stk.append(data)
        return len(stk)



