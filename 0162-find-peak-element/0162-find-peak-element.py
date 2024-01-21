class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #can apply binary search here as no two elemets adjacent have same vaue so we can eliminate the downward half side from any point.
        
        #note that binary search leans towards left so in order to keep the gap moving modify lo to be mid+1
        lo,hi=0,len(nums)-1
        
        
        while lo<hi:
            mid = lo + (hi-lo)//2
            
            if nums[mid]>nums[mid+1]:
                hi=mid #this is not mid+1as if mid is the peak in first itr this discards it
            else:
                lo=mid+1
        return hi
            
            
        