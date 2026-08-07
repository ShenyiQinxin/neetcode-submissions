class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #
        need_map = Counter(t)
        have_map = defaultdict(int)
        have = 0 
        need = len(need_map)
        #
        min_sub_len = float('inf')
        substring = ''
        #
        l=0

        for r in range(len(s)):
            if s[r] in need_map:
                have_map[s[r]] += 1
                if have_map[s[r]] == need_map[s[r]]:
                    have+=1

            while have == need:
                if r-l+1 < min_sub_len:
                    min_sub_len = r-l+1
                    substring = s[l:r+1]
          
                if s[l] in need_map:
                    have_map[s[l]] -= 1
                    # drop *have* when not match with the *need*
                    if have_map[s[l]] < need_map[s[l]]:
                        have -= 1
                l+=1
 
        return substring

        