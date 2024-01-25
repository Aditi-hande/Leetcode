class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        dp=defaultdict(tuple)
        m=len(matrix[0])
        n=len(matrix)
        di=[[1,0],[0,1],[-1,0],[0,-1]]
        
        def getlen(i,j):
            
            if (i,j) in dp:
                return dp[(i,j)]
            l=0
            for ic,jc in di:
                if i+ic in range(0,n) and j+jc in range(0,m) and matrix[i+ic][j+jc]>matrix[i][j]:
                    l=max(l,getlen(ic+i,jc+j))
            dp[(i,j)]=l+1

            return dp[(i,j)]

        ans=0    
        for i in range(n):
            for j in range(m):
                ans=max(ans,getlen(i,j))
        
        return ans
                
                    
                
                
                    