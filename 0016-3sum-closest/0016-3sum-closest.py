class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        ans=None
        mindiff=math.inf
        nums.sort()
        
        for i in range(len(nums)):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            
            l=i+1
            r=len(nums)-1
            
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if abs(target-s)<mindiff:
                    mindiff=abs(target-s)
                    ans=s
                
                if s>target:
                    r-=1
                elif s<target:
                    l+=1
                if s==target:
                    return s
        return ans
                
            
        