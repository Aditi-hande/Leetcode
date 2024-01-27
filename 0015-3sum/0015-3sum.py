class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        
        nums.sort()
        
        for i in range(len(nums)):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            
            l=i+1
            r=len(nums)-1
            
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                
                if s>0:
                    r-=1
                elif s<0:
                    l+=1
                if s==0:
                    ans.append([nums[i],nums[l],nums[r]])
                    l+=1
                    
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return ans
                    
            
      
        
        
# See two sum 2 to see why we have an advantage in orting array
# note: we always skip same elements from the left end to avoid duplicates
#O(n2)
        
        
        