class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_freq = Counter(t)
        win_freq = defaultdict(int)
        have = 0 # count how many unique required char that the win_freq has
        min_len = float('inf')
        l = r = 0
        substring = ''

        for r in range(len(s)):
            if s[r] in need_freq:
                win_freq[s[r]] += 1
                if win_freq[s[r]] == need_freq[s[r]]:
                    have += 1

            while have == len(need_freq): 
                if r-l+1 < min_len:
                    min_len = r-l+1
                    substring = s[l:r+1]
                if s[l] in need_freq:
                    win_freq[s[l]] -= 1
                    if win_freq[s[l]] < need_freq[s[l]]:
                        have -= 1
                
                l+=1
        
        return substring