class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = defaultdict(int)
        max_freq_len = 0
        max_repeat_len = 0
        l = 0

        for r in range(len(s)):
            freq_map[s[r]] += 1
            max_freq_len = max(max_freq_len, freq_map[s[r]])

            while l < r and max_freq_len + k < r - l + 1: # If max_count + k exceeds the window length, it just means you have replacements to spare.
                freq_map[s[l]] -= 1
                l+=1
            max_repeat_len = r - l + 1
        return max_repeat_len
            



        