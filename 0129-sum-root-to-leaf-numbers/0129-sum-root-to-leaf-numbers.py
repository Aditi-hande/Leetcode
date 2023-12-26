# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        ans=0

        st=deque()
        st.append([root,root.val])

        while st:
            # print()
            temp= st.pop()
            # print(temp[1])
            if temp[0].right!=None:
                # print(temp[0].right,temp[0].val)
                # print(temp[0].right.val)
                st.append([temp[0].right,str(temp[1])+str(temp[0].right.val)])
            if temp[0].left!=None:
                st.append([temp[0].left,str(temp[1])+str(temp[0].left.val)])
            if not temp[0].left and not temp[0].right:
                ans+=int(temp[1])
        return ans


        