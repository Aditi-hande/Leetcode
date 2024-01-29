class Solution:
    def trap(self, height: List[int]) -> int:
        
        mleft=0
        mright=0
        ans=0
        
        l=0
        r=len(height)-1
        
        while(l<r):
            
            #filling from left
            
            if height[l]<=height[r]:
                if height[l]>mleft:
                    mleft=height[l]
                else:
                    ans+=(mleft-height[l])
                l+=1
            else:
                #filling from right
                if height[r]>mright:
                    mright=height[r]
                else:
                    ans+=(mright-height[r])
                r-=1
        return ans
                    
                
        