class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        sum1= sum(ord(char) for char in s1)
        sum2= sum(ord(char) for char in s2)
        
        
        s1=sorted(s1)
        s2=sorted(s2)
        
        if sum1>sum2:
            for i in range(len(s1)):
                if s1[i]<s2[i]:
                    return False
        else:
            for i in range(len(s1)):
                if s1[i]>s2[i]:
                    return False
        return True
            
            
        
        