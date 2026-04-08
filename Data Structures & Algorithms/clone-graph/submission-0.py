"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        seen = {node.val: Node(node.val)}
        queue = deque([node])

        while queue:
            real_node = queue.popleft()
            cloned_node = seen[real_node.val]

            for neighbor in real_node.neighbors:
                if neighbor.val not in seen:
                    seen[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)
                cloned_node.neighbors.append(seen[neighbor.val])

        return seen[node.val]
        