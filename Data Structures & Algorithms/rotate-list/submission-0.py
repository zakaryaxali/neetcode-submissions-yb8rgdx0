# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head:
            stack = deque([head])
            while stack[-1].next:
                stack.append(stack[-1].next)
            n = len(stack)
            if n == 1:
                return head

            k = k%n

            if k!=0:
                stack[-1].next = stack[0]
                stack[n-k-1].next=None

                return stack[n-k]
            else:
                return stack[0]
        return None
        