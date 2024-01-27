class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        ans=[1] #will always have it
        
        while len(ans)<n:
            num=ans[-1]*10 #adding zero
             
            while num>n:#if that caused it to exceed undo
                num=num//10
                num=num+1 
                
                while num%10 ==0: #in the case where 199->200 when we need to restart from 2
                    num=num//10 
            ans.append(num)
            
        return ans
            
            
        