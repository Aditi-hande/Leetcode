# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        q=deque()
        q.append([root,0,0])

        lookup={}

        while(q):
            temp,di,dp=q.popleft()
            if lookup.get(tuple([di,dp])):
                lookup.get(tuple([di,dp])).append(temp.val)
                lookup.get(tuple([di,dp])).sort()
            else:
                lookup[tuple([di,dp])]=[temp.val]


            if temp.left:
                q.append([temp.left,di-1,dp+1])
            if temp.right:

                q.append([temp.right,di+1,dp+1])

        # lookup=sorted(lookup.keys(),key=lambda x:(x[0][0],x[0][1]))

        res = defaultdict(list)
        keys = sorted(list(lookup.keys()), key=lambda x: (x[0], x[1]))
        
        
        for k in keys:
            pos, depth = k
            res[pos].extend(lookup[k])

        return res.values()


            

        
        