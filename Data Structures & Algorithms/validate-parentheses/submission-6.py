class Solution:
    def isValid(self, s: str) -> bool:
        store = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                store.append(i)
            else:
                if(len(store) == 0):
                    return False
                top = store.pop()
                if top == '(' and i != ')':
                    return False
                elif top == '{' and i != '}':
                    return False
                elif top == '[' and i != ']':
                    return False
        return len(store) == 0

        