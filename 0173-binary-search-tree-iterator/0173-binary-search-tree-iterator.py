# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    
    def addleft(self, node):
        while node:
            self.st.append(node)
            node=node.left

    def __init__(self, root: Optional[TreeNode]):
        self.st=[]
        self.addleft(root)
             

    def next(self) -> int:
        n=self.st.pop()
        self.addleft(n.right)
        return n.val     
        

    def hasNext(self) -> bool:
        if len(self.st)>0:
            return True
        return False
    

 
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()