class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start, minlen = 0, float('inf')
        t_map, win_map = Counter(t), defaultdict(int)
        need, have = len(t_map), 0
        l = 0
        for r in range(len(s)):
            win_map[s[r]]+=1
            if t_map[s[r]] == win_map[s[r]]:
                have +=1
                
            while need == have:
                if r-l+1 < minlen:
                    minlen = r-l+1
                    start = l
                win_map[s[l]] -= 1
                if t_map[s[l]] > win_map[s[l]]:
                    have -= 1
                l+=1
        return s[start:minlen+start] if minlen != float('inf') else ''


        