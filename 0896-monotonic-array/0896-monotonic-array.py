class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        if not nums:
            return True
        
        incFlag=None
        
        for i in range(len(nums)-1):
            if incFlag==None:
                if nums[i]<nums[i+1]:
                    incFlag=True
                elif nums[i]>nums[i+1]:
                    incFlag=False
            else:
                if nums[i]<nums[i+1] and not incFlag:
                    return False
                if nums[i]>nums[i+1] and incFlag:
                    return False
        return True
            
        