# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth==1:
            newn=TreeNode(val,root)
            return newn
        
        q=deque()
        q.append(root)
        d=1
        
        while q and d!=depth-1:
            for i in range(len(q)):
                temp=q.popleft()


                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            d+=1
        
        while q:
            n=q.popleft()
            newnleft = TreeNode(val)
            newnright = TreeNode(val)
            
            newnleft.left, n.left = n.left, newnleft
            newnright.right, n.right = n.right, newnright
            
            


        return root
            
        
            
        