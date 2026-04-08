# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        
        def dfs(node,arr=set()):
            nonlocal count
            arr.add(node.val)
            print(node.val, arr)
            if node.val>=max(arr):
                count+=1
            if node.left:
                dfs(node.left,arr.copy())
            if node.right:
                dfs(node.right,arr.copy())
        dfs(root)
        return count