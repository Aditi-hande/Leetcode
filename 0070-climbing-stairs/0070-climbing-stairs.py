class Solution:
    def climbStairs(self, n: int) -> int:
        prev=1
        cur=2
        if(n==2):
            return 2
        if(n==1):
            return 1
        if(n==0):
            return 0
        for i in range(0,n-2):
            ans=prev+cur
            prev=cur
            cur=ans
        return ans
        