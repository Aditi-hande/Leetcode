# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        mp= defaultdict(list)
        
        def dfs(node,prev):
            if not node:
                return
            if prev!=None:
                mp[node.val].append(prev)
            prev=node
            
            if node.left:
                mp[node.val].append(node.left.val)
                dfs(node.left,node.val)
                
            if node.right:
                mp[node.val].append(node.right.val)
                dfs(node.right,node.val)
        
        dfs(root,None)
        # print(mp)
        
        res=[]
        q=deque()
        q.append((target.val,0))
        visit=set()
        visit.add(target.val)
        
        while q:
            ele,dist = q.popleft()
            # print(ele,dist,res)
            
            if dist==k:
                res.append(ele)
            else:
                for nbr in mp[ele]:
                    if nbr not in visit:
                        visit.add(nbr)
                        q.append((nbr,dist+1))
        return res
                        
                                
        