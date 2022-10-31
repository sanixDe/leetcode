# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        
        dict = {}
        
        cur = head
        while cur:
            
            dict[cur.val] = 1 + dict.get(cur.val, 0)
            
            cur = cur.next
        
        dummy = ListNode()
        
        cur1 = dummy
        cur = head
        while cur:
            
            if dict[cur.val] == 1:
                cur1.next = ListNode(cur.val)
                cur1 = cur1.next
            cur = cur.next
        return dummy.next
            
            