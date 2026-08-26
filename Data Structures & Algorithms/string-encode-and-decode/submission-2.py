class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = ''
        for s in strs:
            encoded_str = str(len(s)) + '#' + s
            encoded_strs += encoded_str
        # print(encoded_strs)
        return encoded_strs


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            s_len = int(s[i:j])
            res.append(s[j+1:j+1+s_len])
            i = j+1+s_len
        return res
        
