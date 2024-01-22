class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            cpy=x
        else:
            cpy=-x
        ans=0
        
        while cpy>0:
            unit=cpy%10
            ans=ans*10+unit
            cpy=cpy//10
        
        if ans>= pow(-2,31) and ans<=pow(2,31)-1:
            return -ans if x<0 else ans
        else:
            return 0
            
        