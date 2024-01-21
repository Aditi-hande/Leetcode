class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
#         map=collections.defaultdict(list)
        
#         for i in range(len(strs)):
#             temp=str(Counter(strs[i]))
#             # temp=''.join(sorted(strs[i]))
#             map[temp].append(strs[i])
            
#         for str1 in strs:
#             print(str1,Counter(str1),str(Counter(str1)))
            
#         return list(map.values())

        d = collections.defaultdict(list)
        y = Counter('abcdefghijklmnopqrstuvwxyz')
        for s in strs:
            z = Counter(y) + Counter(s)
            # print(z)
            key = ''.join(str(z.values()))
            # print(type(key))
            d[key].append(s)

        return d.values()