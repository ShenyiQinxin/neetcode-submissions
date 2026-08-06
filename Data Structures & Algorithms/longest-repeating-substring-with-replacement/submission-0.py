class Solution:
    # aabbc
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = -1
        freq_map = defaultdict(int)
        longest = 0

        l = r = 0

        while r < len(s):
            freq_map[s[r]] += 1
            max_freq = max(max_freq, freq_map[s[r]])
            r+=1

            while r-l - max_freq > k:
                freq_map[s[l]] -= 1
                l+=1
            longest = max(longest, r-l)
        return longest


