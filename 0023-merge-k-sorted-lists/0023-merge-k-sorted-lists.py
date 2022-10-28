# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        
        for i in range(len(lists)):
            
            cur = lists[i]
            
            while cur:
                nodes.append(cur.val)
                cur = cur.next
        head = cur = ListNode()
        for x in sorted(nodes):
            cur.next = ListNode(x)
            cur = cur.next
        return head.next