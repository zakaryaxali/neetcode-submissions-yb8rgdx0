# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        root=TreeNode(preorder[0])
        n = len(preorder)
        if n==1:
            return root

        mid = inorder.index(root.val)
        if mid!=0:
            ileft = inorder[:mid]
            root.left = buildTree(_, left)
        if mid!=n-1:
            right = inorder[mid+1:]
            root.right = buildTree(_, right)
        return root




        