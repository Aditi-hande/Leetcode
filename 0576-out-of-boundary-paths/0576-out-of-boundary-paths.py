class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp={}
        
        def rec(i,j,moves):
            if (i,j,moves) in dp:return dp[(i,j,moves)]
            if i>=m or j>=n or i<0 or j<0:
                return 1
            elif moves == 0:
                return 0
            ans = rec(i+1,j,moves-1)
            ans += rec(i-1,j,moves-1)
            ans += rec(i,j+1,moves-1)
            ans += rec(i,j-1,moves-1)
            dp[(i,j,moves)]=ans
            return dp[(i,j,moves)]
        return rec(startRow,startColumn,maxMove) %(10**9+7)
            
            
        
        
        