class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        res = ''
        N = len(s)

        for i in range(N):
            left, right = i, i
            while 0<=left and right<N and s[left]==s[right]:
                if right-left+1>longest:
                    longest = right-left+1
                    res = s[left:right+1]
                left-=1
                right+=1
            left, right = i, i+1
            while 0<=left and right<N and s[left]==s[right]:
                if right-left+1>longest:
                    longest = right-left+1
                    res = s[left:right+1]
                left-=1
                right+=1
        return res

            

        