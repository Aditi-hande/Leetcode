class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties = sorted(properties,key=lambda x:(-x[0],x[1]))
        #first by desc and second by asc
        ans=0
        maxele=0
        for a,d in properties:
            if d<maxele:
                ans+=1
            else:
                maxele=d
        return ans
            
        
        