class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        
        mp={"1":"","2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        
        res=[]
        
        def getstr(i,strsofar):
            if i==len(digits):
                res.append(strsofar)
                return
            # print(i)
                
            for c in mp[digits[i]]:
                getstr(i+1,strsofar+c)
        
        getstr(0,"")
        return res
                
        