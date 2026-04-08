# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a,b = l1,l2
        root = ListNode()
        prev = root
        retenue = 0

        while a or b or retenue:
            value=retenue
            retenue=0
            if a:
                value += a.val
                a=a.next
            
            if b:
                value += b.val
                b=b.next
            
            if value>=10:
                value-=10
                retenue=1

            current = ListNode(value)
            prev.next=current
            prev = current
        
        return root.next
        