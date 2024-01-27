# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        self.idx=-1
        self.order=[]
        
        def inorder(n):
            if n.left:
                inorder(n.left)
            self.order.append(n.val)
            
            if n.right:
                inorder(n.right)
                
        inorder(root)
        

    def next(self) -> int:
        self.idx+=1
        return self.order[self.idx]
        
        

    def hasNext(self) -> bool:
        if self.idx+1>=len(self.order):
            return False
        else:
            return True
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()