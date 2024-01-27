class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        ans=[]
        
        while l<r:
            s=numbers[l]+numbers[r]
            if s==target:
                ans.append(l+1)
                ans.append(r+1)
                return ans
                
            if s>target:
                r-=1
            else:
                l+=1
        return ans
                
        
        
        
        
        