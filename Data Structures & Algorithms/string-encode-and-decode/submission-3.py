class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        # print(res)
        return res
            

    def decode(self, s: str) -> List[str]:
        arr = []
        i = 0
        while i < len(s):
            j=i
            while s[j] != '#':
                j+=1
            s_len = int(s[i:j])
            arr.append(s[j+1:j+1+s_len])
            i = j+s_len+1
        return arr
        
