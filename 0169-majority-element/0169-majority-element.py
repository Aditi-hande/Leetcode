class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frq={}
        for i in range (len(nums)):
            if nums[i] in frq:
                frq[nums[i]]+=1
            else:
                frq[nums[i]]=1
        # print(frq)
        return max(frq,key=frq.get)
