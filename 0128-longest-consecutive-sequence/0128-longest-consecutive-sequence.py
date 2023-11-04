class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        myset=set(nums)
        mans=1
        ans=1
        for i in range(0,len(nums)):
            if nums[i]-1 not in myset:
                temp=nums[i]+1
                while(temp in myset):
                    ans=ans+1
                    temp=temp+1
                mans=max(mans,ans)
                ans=1
        return mans
                
                    
        