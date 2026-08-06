class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list)
        
        for s in strs:
            s_counter = Counter(s)
            key = tuple(sorted(s_counter.items()))
            
            str_map[key].append(s)
        return list(str_map.values())
        
