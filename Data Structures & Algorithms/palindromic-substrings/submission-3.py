class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        counter = 0

        for i in range(n):
            l = r = i
            while 0 <= l and r < n and s[l] == s[r]:
                counter += 1
                l-=1
                r+=1
                
            l, r = i, i+1
            while 0 <= l and r < n and s[l] == s[r]:
                counter += 1
                l-=1
                r+=1
        return counter
            
        