class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        
        lz,i=0,0
        
        while i<len(nums):
            if nums[i]==0:
                i+=1
            else:
                temp=nums[lz]
                nums[lz]=nums[i]
                nums[i]=temp
                lz+=1
                i+=1
                
                