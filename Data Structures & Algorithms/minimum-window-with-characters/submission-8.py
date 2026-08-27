class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_map = Counter(t)
        need = len(need_map)
        met = 0
        min_len = float('inf')
        min_len_start = 0
        l = 0

        for r in range(len(s)):
            need_map[s[r]] -= 1
            if need_map[s[r]] == 0:
                met += 1
            
            while met == need:
                if r - l + 1 < min_len:
                    min_len = r-l+1
                    min_len_start = l
                need_map[s[l]] += 1
                if need_map[s[l]] > 0: # broken the met criteria
                    met -= 1
                l+=1
        return s[min_len_start:min_len_start+min_len] if min_len != float('inf') else ''
                

        