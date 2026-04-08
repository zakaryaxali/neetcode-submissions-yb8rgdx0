# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        el1=list1
        el2=list2
        result = []

        while el1 or el2:
            if (el1 and not el2) or (el1 and el1.val <= el2.val):
                result.append(el1)
                el1=el1.next
            else:
                result.append(el2)
                el2=el2.next

        for i in reversed(range(len(result)-1)):
            result[i].next = result[i+1]

        return result[0] if result else None