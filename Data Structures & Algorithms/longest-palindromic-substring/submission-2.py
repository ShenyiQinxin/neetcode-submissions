class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = 0
        start = 0

        for i in range(n):
            l = r = i
            while 0 <= l and r < n and s[l] == s[r]:
                if r-l+1 > longest:
                    longest = r-l+1
                    start = l

                l-=1
                r+=1

    
            l, r = i, i+1
            while 0 <= l and r < n and s[l] == s[r]:
                if r-l+1 > longest:
                    longest = r-l+1
                    start = l
                l-=1
                r+=1

        return s[start:longest+start]
            
            


        