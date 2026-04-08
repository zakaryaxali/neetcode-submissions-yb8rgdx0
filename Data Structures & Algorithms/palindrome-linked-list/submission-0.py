# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        queue = deque([])
        node=head
        while node:
            queue.append(node)
            node=node.next

        if len(queue)==1:
            return True

        first = queue.popleft()
        last = queue.pop()
        while first and last:
            if first.val != last.val:
                return False
            if queue:
                first=queue.popleft()
            else:
                break
            if queue:
                last=queue.pop()
            else:
                break
            

        return True