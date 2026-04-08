# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i=0
        start =ListNode(0,head)
        if n==1:
            return head.next
        parent = start
        node=head

        while i<n:
            parent = node
            node=node.next
            i+=1

        if not node:
            start = ListNode(0,parent)
        elif node.next==None:
            parent.next=None
        else:
            parent.next=node.next

        return start.next