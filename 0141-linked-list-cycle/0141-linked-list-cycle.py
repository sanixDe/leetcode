# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # visited = {}; fin = False
        # temp = head;
        # while(temp != None):
        #     if (temp.next in visited):
        #         fin = True; break;
        #     else: visited[temp.next] = 1;
        #     temp = temp.next;
        # return fin;
        
        visited = set()
        
        cur = head
        while cur:
            if cur in visited:
                return True
            visited.add(cur)
            cur = cur.next
        return False