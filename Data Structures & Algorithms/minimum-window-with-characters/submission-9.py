class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = Counter(t)
        t_len = len(t_map)
        win_map = defaultdict(int)
        formed = 0
        min_win_len = float('inf')
        min_win_start = 0

        l = 0
        for r in range(len(s)):
            win_map[s[r]]+=1
            if win_map[s[r]] == t_map[s[r]]:
                formed+=1

            while formed == t_len:
                if r-l+1 < min_win_len:
                    min_win_len = r-l+1
                    min_win_start = l
                win_map[s[l]] -= 1
                if win_map[s[l]] < t_map[s[l]]:
                    formed-= 1

                l+=1
        return s[min_win_start:min_win_len+min_win_start] if min_win_len != float('inf') else ''

            
        