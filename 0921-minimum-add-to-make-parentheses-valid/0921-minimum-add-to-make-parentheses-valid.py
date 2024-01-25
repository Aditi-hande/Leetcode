class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans,bal=0,0
        
        for char in s:
            if char=='(':
                bal+=1
            else:
                bal-=1
            
            if bal==-1:
                ans+=1
                bal=0
        return ans+bal
            
        
        

        