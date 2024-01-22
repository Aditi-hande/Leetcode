class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        s=set(nums)
        ans=0
        maxans=0
        
        for num in nums:
            if num-1 not in s: # start of sequence
                ans=0
                while num in s:
                    ans+=1
                    num+=1
            maxans=max(maxans,ans)
        
        return maxans
        