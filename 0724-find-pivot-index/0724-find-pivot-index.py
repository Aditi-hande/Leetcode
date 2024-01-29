class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s=sum(nums)
        
        
        ss=0
        
        for i in range(len(nums)):
            
            if i!=0: 
                ss+=nums[i-1]
            if ss==(s-nums[i])/2:
                return i
            
        return -1
            
            
        

                