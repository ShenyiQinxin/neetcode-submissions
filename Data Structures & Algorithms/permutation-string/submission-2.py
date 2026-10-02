class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_map = Counter(s1)

        if len(s1) == len(s2):
            return Counter(s2) == s1_map

        match = 0
        win_map = defaultdict(int)
        l = 0
        for r in range(len(s2)):
            win_map[s2[r]] += 1
            if s1_map[s2[r]] == win_map[s2[r]]:
                match+=1
            elif s1_map[s2[r]] +1 == win_map[s2[r]]:
                match-=1
            
            if r-l+1 > len(s1):
                win_map[s2[l]]-=1
                if s1_map[s2[l]] == win_map[s2[l]]:
                    match+=1
                elif s1_map[s2[l]] == win_map[s2[l]]+1:
                    match-=1

                l+=1

            if match == len(s1_map):
                return True
        return False
            
        