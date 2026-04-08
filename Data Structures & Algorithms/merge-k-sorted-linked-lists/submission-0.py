# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Node(ListNode):
    def __init__(self, node):
        super().__init__(node.val,node.next)
        self.node = node

    def __lt__(self, other):
        return self.val < other.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        heapq.heapify(nodes)
        for node in lists:
            if node:
                heapq.heappush(nodes, Node(node))
        
        dummy = ListNode(0)
        curr = dummy
        while nodes:
            wrapper = heapq.heappop(nodes)
            curr.next = wrapper.node  # attach the actual ListNode
            curr = curr.next
            if wrapper.node.next:
                heapq.heappush(nodes, Node(wrapper.node.next))
        
        return dummy.next
