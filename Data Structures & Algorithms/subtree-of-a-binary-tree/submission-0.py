# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 1. find if head of subroot in root tree
        # 2. then check node one by one
        # 3. 
        def same_trees(a,b):
            if a and b and a.val == b.val:
                return same_trees(a.left,b.left) and same_trees(a.right,b.right)
            elif a is None and b is None:
                return True
            else:
                return False

        stack = deque([root])

        while stack:
            node = stack.pop()
            if same_trees(node, subRoot):
                return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return False



        