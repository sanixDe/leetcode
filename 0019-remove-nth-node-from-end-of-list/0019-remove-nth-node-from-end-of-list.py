# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # first let's find the len of the list
        
        cur = head
        
        for i in range(n):
            cur = cur.next
        
        if cur == None:
            return head.next
        nodeBefore = head
        while cur.next:
            cur = cur.next
            nodeBefore = nodeBefore.next
        
        nodeBefore.next = nodeBefore.next.next
        
        return head
        