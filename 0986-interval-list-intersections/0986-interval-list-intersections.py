class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        i=j=0
        ans=[]
        
        while i<len(firstList) and j<len(secondList):
            fend,fstart=firstList[i][1],firstList[i][0]
            send,sstart=secondList[j][1],secondList[j][0]
            
            if fstart<=send and sstart<=fend: #remember criss cross
                ans.append([max(sstart,fstart),min(fend,send)])
            
            if fend<=send:
                i+=1
            else:
                j+=1
                
        return ans
                

                
        