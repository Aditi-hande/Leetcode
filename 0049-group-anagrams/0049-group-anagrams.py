class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map=collections.defaultdict(list)
        
        for i in range(len(strs)):
            temp=''.join(sorted(strs[i]))
            map[temp].append(strs[i])
            
        return list(map.values())
        