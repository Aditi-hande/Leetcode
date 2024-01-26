class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i=click[0]
        j=click[1]
        di=[[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,-1],[-1,1],[1,-1]]
        m=len(board) #i
        n=len(board[0]) #j

        def getcnt(r,c):
            cnt=0
            for dr,dc in di:
                if r+dr in range(m) and c+dc in range(n):
                    if board[r+dr][c+dc]=='M':
                        cnt+=1
            return cnt



        def dfs(r,c):
            if board[r][c]!='E':
                return

            mines=getcnt(r,c)

            if mines!=0:
                board[r][c]=str(mines)
                return
            else:
                board[r][c]='B'
                for dr,dc in di:
                    if r+dr in range(m) and c+dc in range(n):
                        dfs(r+dr,c+dc)
        
        if board[i][j]=='M':
            board[i][j]='X'
            return board
        if board[i][j]=='B':
            return board

        dfs(i,j)
        return board
        
        
        
        