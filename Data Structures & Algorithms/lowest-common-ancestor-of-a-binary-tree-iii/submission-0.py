"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pstack = deque([])
        qstack = deque([])
        node = p
        while node:
            pstack.append(node)
            node = node.parent
        node = q
        while node:
            qstack.append(node)
            node = node.parent
        # print([item.val for item in pstack])
        # print([item.val for item in qstack])
        while pstack:
            node = pstack.popleft()
            if node in qstack:
                return node 
        