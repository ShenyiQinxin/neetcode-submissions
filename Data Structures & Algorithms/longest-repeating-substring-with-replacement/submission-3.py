class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = defaultdict(int)
        max_freq = 0
        l = 0
        r = 0

        while r < len(s):
            freq_map[s[r]] += 1
            max_freq = max(max_freq, freq_map[s[r]])

            while max_freq + k < r-l+1:
                freq_map[s[l]] -= 1
                l+=1
            r+=1
        return r-l





        