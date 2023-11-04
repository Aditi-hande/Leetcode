class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        myset=set(nums)
        mans=1
        ans=1
        for num in nums:
            if num-1 not in myset:
                temp=num+1
                while(temp in myset):
                    ans=ans+1
                    temp=temp+1
                mans=max(mans,ans)
                ans=1
        return mans
                
                    
        