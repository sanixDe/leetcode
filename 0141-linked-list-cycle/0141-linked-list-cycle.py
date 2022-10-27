# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
#         visited = set()
        
#         cur = head
#         while cur:
#             if cur in visited:
#                 return True
#             visited.add(cur)
#             cur = cur.next
#         return False
#         Time complexity = O(N)
#         Space complexity = O(N)

        fast = slow = head
        flag = 0
        while fast and fast.next:
            if fast == slow and flag == 1:
                return True
            slow = slow.next
            fast = fast.next.next
            flag = 1
            
        return False