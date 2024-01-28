class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid[0]) #i
        m=len(grid) #j
        di=[(0,1),(1,0),(-1,0),(0,-1)]
        
        #flip 1s in a island
        def dfs(i,j):
            if i not in range(m) or j not in range(n) or grid[i][j]=="0":
                return
            grid[i][j]="0"
            
            for r,c in di:
                dfs(r+i,c+j)
      
        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    dfs(i,j)
                    ans+=1
        return ans
                    
        