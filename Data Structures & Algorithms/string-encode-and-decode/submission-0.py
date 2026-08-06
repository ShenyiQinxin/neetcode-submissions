class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = ''
        for s in strs:
            encode_s = str(len(s)) + '#' + s
            encoded_strs += encode_s
        print(encoded_strs)
        return encoded_strs


    def decode(self, encoded_strs: str) -> List[str]:
        rst = []
        i = 0
        while i < len(encoded_strs):
            j = i
            while encoded_strs[j] != '#':
                j += 1
            #j is a #
            s_len = int(encoded_strs[i:j])
            s = encoded_strs[j+1:j+1+s_len]
            rst.append(s)
            i= j+1+s_len
        return rst




                


