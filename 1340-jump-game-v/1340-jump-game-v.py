class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        
        dp = dict()
        def dfs(i,arr):
            if i in dp: return dp[i]
            pathlen = 0
            for j in range(i + 1, i + d + 1):
                if len(arr) <= j or arr[j] >= arr[i]: break
                pathlen = max(dfs(j,arr), pathlen)
            for j in range(i-1, i-d-1,-1):
                if j < 0 or arr[j] >= arr [i]: break
                pathlen = max(dfs(j,arr), pathlen)  
            dp[i] = pathlen + 1
            return dp[i]
        
        longestpath = 0
        for i in range(len(arr)):
            longestpath = max(dfs(i,arr),longestpath)
        return longestpath
    
#         self.dp=defaultdict(int)
#         self.d=d
#         self.lenarr=len(arr)
#         self.arr=arr
#         ans=0
#         for i in range(len(arr)):
#             ans=max(self.imax(i),ans)
#         print(self.dp)
#         return ans
        
#     def imax(self,i):
#         di=[-1,1]
#         ans=0
#         if i not in self.dp:
#             for dire in di :
#                 for j in range(1,self.d+1):
#                     if (i+dire*j) in range(0,self.lenarr) and self.arr[i+dire*j]<self.arr[i]:
#                         ans=max(ans,self.imax(i+dire*j))
#                     # else:
#                     #     break

#             self.dp[i]=ans+1
#             return self.dp[i]
                        
#         else:
#             return self.dp[i]
#         #not able to understand why, if else break is removed why wrong answerr?
        
        