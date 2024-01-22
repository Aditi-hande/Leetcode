class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        s=str(x)
        lo,hi=0,len(s)-1
        
        while(lo<=hi):
            if s[lo]!=s[hi]:
                return False
            lo+=1
            hi-=1
        return True
        