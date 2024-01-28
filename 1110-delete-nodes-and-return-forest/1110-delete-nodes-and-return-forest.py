# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        delset=set(to_delete)
        
        ans=[]
        
        def getans(node,parentdel):
            if not node:
                return
            selfdel = node.val in delset
            
            if parentdel and not selfdel:
                ans.append(node)
                
            node.left = getans(node.left,selfdel)
            node.right = getans(node.right,selfdel)
            
            if selfdel:
                return None
            else:
                return node
            
            
        getans(root,True)
        return ans  
        