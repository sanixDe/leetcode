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
        
        '''
        Three steps
            -> Finding the middle element in linked list
            -> After that reverse the second linkedlist (middle - end)
            -> Merge two linkedlists
        
        '''
        
        # STEP 1 finding the middle node with fast and slow pointer
        
        slow = fast = head
        
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
        
        # STEP 2 reversing the second linkedlist
        
        cur = slow
        pre = None
        
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
            
            # pre, cur, cur.next = pre, cur.next, cur
            
        # Step 3 merging the linkedlist
        
        first = head
        second = pre
        
        while second.next:
            
            first.next, first = second, first.next
            second.next, second = first, second.next
            
        
        
        '''
        Time Complexity = O(N)
        Space Complexity = O(N)
        '''