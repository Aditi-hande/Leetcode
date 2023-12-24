class Solution:
    def chkpal(self, s:str)->bool:
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True

    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                # print(s[l+1:r+1], s[l:r],l,r)
                return self.chkpal(s[l+1:r+1]) or self.chkpal(s[l:r])
            l+=1
            r-=1
        return True



        
        