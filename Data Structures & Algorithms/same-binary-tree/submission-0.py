# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        pstack = deque([p])
        qstack = deque([q])

        while pstack and qstack:
            a = pstack.pop()
            b = qstack.pop()

            if a.val == b.val:
                if a.left and b.left:
                    pstack.append(a.left)
                    qstack.append(b.left)
                elif (a.left and not b.left) or (b.left and not a.left):
                    return False
                if a.right and b.right:
                    pstack.append(a.right)
                    qstack.append(b.right)
                elif (a.right and not b.right) or (b.right and not a.right):
                    return False
            else:
                return False


        return len(pstack)==len(qstack)
        