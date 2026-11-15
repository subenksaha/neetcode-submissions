# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for head in lists:
            heapq.heappush(heap, NodeWrapper(head))
        
        dummy = ListNode()
        curr = dummy
        while heap:
            poped = heapq.heappop(heap)
            curr.next = poped.node
            curr = curr.next
            if poped.node.next:
                n = poped.node.next
                heapq.heappush(heap, NodeWrapper(n))
        
        return dummy.next