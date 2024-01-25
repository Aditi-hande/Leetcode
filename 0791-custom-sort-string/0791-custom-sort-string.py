class Solution:
    def customSortString(self, order: str, s: str) -> str:
        map=Counter(s)
        ans=""
       
        
        for char in order:
            if char in map:
                for i in range(map[char]):
                    ans=ans+char
                map[char]=0

        for ele in map:
            for i in range(map[ele]):
                ans+=ele
            map[ele]=0
            
        return ans
        