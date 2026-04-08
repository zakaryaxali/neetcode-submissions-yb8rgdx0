# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node, val):
            if node.val > val:
                if node.left:
                    dfs(node.left, val)
                else:
                    node.left=TreeNode(val)
                    
            if node.val < val:
                if node.right:
                    dfs(node.right, val)
                else:
                    node.right=TreeNode(val)
        if root:
            dfs(root, val)
            return root
        else:
            return TreeNode(val)
                    