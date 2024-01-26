# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q=deque()
        q.append(root)
        
        lleaf,rleaf=None,None
        
        while q:
            fflag=True
            for _ in range(len(q)):
                node= q.popleft()
                
                if fflag:
                    lleaf=node
                fflag=False
                rleaf=node
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
        def getlca(root,p,q):
            if p==root or q==root:
                return root
            
            left,right=None,None
            if root.left:
                left=getlca(root.left,p,q)
            if root.right:
                right=getlca(root.right,p,q)
            
            if left and right:
                return root
            return left or right
        
        return getlca(root,lleaf,rleaf)
                
            
        