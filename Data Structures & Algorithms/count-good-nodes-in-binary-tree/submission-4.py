# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        
        def dfs(node,max_):
            nonlocal count
            # print(node.val, arr)
            if node.val>=max_:
                max_=node.val
                count+=1
            if node.left:
                dfs(node.left,max_)
            if node.right:
                dfs(node.right,max_)
        dfs(root,root.val)
        return count