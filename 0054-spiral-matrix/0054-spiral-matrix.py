class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        wid=len(matrix[0])
        hig=len(matrix)
        
        ans=[]
        # ans.append(matrix[0][0])
        
        ver,hor=hig-1,wid
        lasti,lastj=0,-1
        dire= 1
        cnt=0
        while cnt<wid*hig:
            # print(cnt)
            if dire==1:#horizontal and fwd
                
                for _ in range (hor):
                    lastj+=1
                    ans.append(matrix[lasti][lastj])
                    cnt+=1
                hor-=1
                dire=2
                
            elif dire==2:#vertical and dwn
                
                for _ in range(ver):
                    lasti+=1
                    ans.append(matrix[lasti][lastj])
                    cnt+=1
                ver-=1
                dire=3
            elif dire==3:#horizontal back
                
                for _ in range(hor):
                    lastj-=1
                    ans.append(matrix[lasti][lastj])
                    cnt+=1
                hor-=1
                dire=4
                
            else: #vertical upward
                
                for _ in range(ver):
                    lasti-=1
                    ans.append(matrix[lasti][lastj])
                    cnt+=1
                    
                ver-=1
                dire=1
        return ans
        
                
                    
                    
                
        
        
        
        