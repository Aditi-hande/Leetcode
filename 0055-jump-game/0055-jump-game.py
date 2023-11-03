class Solution:
    def canJump(self, nums: List[int]) -> bool:
    
        if(len(nums)==1):
            return True
        prev=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if(nums[i]>=prev-i):
                prev=i
            if(i==0 and nums[i]<prev-i):
                return False
        return True
            
            