# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_=-math.inf

        def dfs(node):
            nonlocal max_
            if not node:
                return
            left=get_max(node.left)
            right=get_max(node.right)
            res=node.val+left+right
            max_=max(max_,res)
            dfs(node.left)
            dfs(node.right)

            
        def get_max(node):
            if not node:
                return 0
            left=get_max(node.left)
            right=get_max(node.right)
            path=node.val+max(left,right)
            return max(0,path)

        dfs(root)
        return max_
