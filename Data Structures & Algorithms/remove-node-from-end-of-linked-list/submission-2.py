# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node=node.next
        
        m = len(nodes)
        print(m)

        if m == 1:
            return ListNode().next
        if n == 1:
            nodes[-2].next = None
            return nodes[0]
        if n == m:
            return nodes[1]

        nodes[-n-1].next = nodes[-n+1]
        return nodes[0]

        

