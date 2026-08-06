class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        win_count = defaultdict(int)
        have = 0 # count how many required char that the win_count has
        min_len = float('inf')
        l = r = 0
        substring = ''

        for r in range(len(s)):
            if s[r] in need:
                win_count[s[r]] += 1
                if win_count[s[r]] == need[s[r]]:
                    have += 1

            while have == len(need): 
                if r-l+1 < min_len:
                    min_len = r-l+1
                    substring = s[l:r+1]
                if s[l] in need:
                    win_count[s[l]] -= 1
                    if win_count[s[l]] < need[s[l]]:
                        have -= 1
                
                l+=1
        


        return substring