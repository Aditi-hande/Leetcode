class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s=set()
        ans=[]
        maxele=len(nums)
        
        for num in nums:
            if num not in s:
                s.add(num)
            else:
                ans.append(num)
            
        
        for i in range(1,maxele+1):
            if i not in s:
                ans.append(i)
        return ans
        
                
        