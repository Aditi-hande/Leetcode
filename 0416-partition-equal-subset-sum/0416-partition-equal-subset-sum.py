class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        s=sum(nums)
        
        if (s%2)!=0:
            return False
        
        sums=set()
        sums.add(0)
        
        for i in range(len(nums)):
            temp=set()
            for ele in sums:
                temp.add(ele)
                temp.add(ele+nums[i])
                if ele+nums[i]==s/2:
                    return True
            sums=temp
        
        return s/2 in sums
                
            


            
        