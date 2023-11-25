class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        temp=0
        ans=[0]*len(nums)
        for i in range(0,len(nums)):
            temp+=abs(nums[0]-nums[i])
        ans[0]=temp
        for i in range(1,len(nums)):
            dif=nums[i]-nums[i-1]
            # print(dif)
            ans[i]=ans[i-1]+(dif*(i))-(dif*(len(nums)-i))
        return ans
            
            
        