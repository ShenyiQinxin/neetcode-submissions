class Solution:
    def reverseBits(self, n: int) -> int:
        res  = 0
        for _ in range(32):
            res = res << 1
            res = res | (n % 2)
            n = n // 2
        return res
        