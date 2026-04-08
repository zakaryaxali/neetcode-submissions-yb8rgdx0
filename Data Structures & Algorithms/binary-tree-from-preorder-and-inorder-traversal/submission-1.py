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

        mid = inorder.index(root.val)
        if mid!=0:
            ileft = inorder[:mid]
            pleft = [item for item in inorder if item in ileft]
            root.left = self.buildTree(pleft, ileft)
        if mid!=n-1:
            iright = inorder[mid+1:]
            pright = [item for item in inorder if item in iright]
            root.right = self.buildTree(pright, iright)
        return root




        