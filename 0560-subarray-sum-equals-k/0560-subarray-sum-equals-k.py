class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum=0
        ans=0
        map=defaultdict(int)
        map[0]=1 # to consider the case where prefix sum is itself k
        
        for i in range(len(nums)):
            presum+=nums[i]
            if (presum-k) in map: # its presum-k as we look backwards in prefix sum since we dont know forward values yet
                ans+=map[presum-k]
            map[presum]+=1
        return ans
        