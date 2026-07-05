class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(str(len(s)))
            result.append('#')
            result.append(s)
        print("".join(result))
        return "".join(result)


    def decode(self, s: str) -> List[str]:
        store = []
        i = 0
        while i < len(s):
            j = i
            while(s[j] != '#'):
                j+=1
            num = int(s[i:j])
            substr = s[j+1: j+1+num]
            store.append(substr)
            i = j+1+num
        return store



