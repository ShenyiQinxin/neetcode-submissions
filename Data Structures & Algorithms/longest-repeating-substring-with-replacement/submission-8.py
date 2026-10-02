class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        longest = 0
        max_repeat = 0
        l = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            max_repeat = max(max_repeat, freq[s[r]])

            if max_repeat+k < r-l+1:
                freq[s[l]]-=1
                l+=1
            longest = max(longest, r-l+1)
        return longest


            

        