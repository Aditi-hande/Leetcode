class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #staying consistent by whenever i add in queue i add in visit (but add in queue only if not in visit)
        #BFS and no weights to the direction
        #checking bounds in first if (insted of writing for both r and c writing for min or max)
        if not grid:
            return -1

        n= len(grid) #since square both same 
        q=deque([(0,0,1)]) # r,c,len
        visited=set((0,0))
        dir=[(0,1),(1,0),(1,1),(-1,0),(0,-1),(-1,-1),(1,-1),(-1,1)]

        while q:
            r,c,l=q.popleft()

            if min(r,c)<0 or max(r,c)>=n  or grid[r][c]==1:
                continue
            elif r==n-1 and c== n-1:
                return l
            else:
                for dr,dc in dir:
                    if (r+dr,c+dc) not in visited:
                        q.append((r+dr,c+dc,l+1))
                        visited.add((r+dr,c+dc))
        return -1
                
                
                



        