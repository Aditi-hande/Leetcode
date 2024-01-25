class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        i=0
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        # print(nums)
        
        minele=math.inf
        minidx=-1
        n=len(nums)
        for i in range(n-1):
            temp=abs(int(nums[i]/(i+1)) - int((nums[-1]-nums[i])/(n-i-1)))
            if temp<minele:
                minele=temp
                minidx=i
                
        temp=int(nums[-1]/n)
        if temp<minele:
            return n-1
    
        
        return minidx
        