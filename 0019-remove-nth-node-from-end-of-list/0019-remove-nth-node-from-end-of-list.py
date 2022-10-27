# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # first let's find the len of the list
        
        cur = head
        l = 0
        while cur:
            cur = cur.next
            l += 1
        # print(l-n)
        
        if l == n:
            return head.next
        # b = 0
        cur = head
        for i in range(0, (l-n-1)):
            cur = cur.next
        
        cur.next = cur.next.next
        
        return head
        