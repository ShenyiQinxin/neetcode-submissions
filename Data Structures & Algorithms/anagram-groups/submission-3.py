class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rst_map = defaultdict(list)

        for s in strs:
            sorted_s = ''.join(sorted(s))
            rst_map[sorted_s].append(s)
        # print(rst_map.values())
        return list(rst_map.values())
        