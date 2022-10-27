# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # finding the middle element
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow
        pre = None
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        
        first, second = head, pre
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
            
            
        
        '''
        Time Complexity = O(N)
        Space Complexity = O(N)
        '''