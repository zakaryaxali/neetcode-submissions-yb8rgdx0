# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        a = deque([])
        node = head
        while node:
            a.append(node)
            node=node.next

        parent = a.popleft()
        child = a.pop()
        parent.next=child
        next_left=True
        while len(a):
            parent=child
            if next_left:
                child=a.popleft()
            else:
                child=a.pop()
            next_left= not next_left
            parent.next=child

        child.next = None