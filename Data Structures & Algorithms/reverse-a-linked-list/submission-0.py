# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        current_node=head
        nodes=[]
        while current_node:
            nodes.append(current_node)
            current_node=current_node.next

        for i in reversed(range(1,len(nodes))):
            nodes[i].next = nodes[i-1]
        
        nodes[0].next = None
        return nodes[-1]
        