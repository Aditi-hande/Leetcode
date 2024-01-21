class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        ans=[]
        for i in range(len(nums)):
            if target-nums[i] in map:
                ans.append(i)
                ans.append(map[target-nums[i]])
                return ans
            map[nums[i]]=i
                
            