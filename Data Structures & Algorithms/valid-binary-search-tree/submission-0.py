# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            node_min=None
            node_max=None
            if not node:
                return node_min,node_max,True

            if node.left:
                min_,max_,valid = dfs(node.left)
                if valid and max_<node.val:
                    node_min=min_
                else:
                    return node_min,node_max,False
            else:
                node_min=node.val
            if node.right:
                min_,max_,valid = dfs(node.right)
                if valid and min_>node.val:
                    node_max=max_
                else:
                    return node_min,node_max,False
            else:
                node_max=node.val
            return node_min,node_max,True

        return dfs(root)[2]

        