class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF # all 32 bits are 1
        while b != 0:
            carry = ((a&b) << 1) & mask
            a = (a ^ b) & mask
            b = carry 
        if a > 0x7FFFFFFF: # largest positive value in 32 bits signed
            a = ~(a^mask)

        return a
        