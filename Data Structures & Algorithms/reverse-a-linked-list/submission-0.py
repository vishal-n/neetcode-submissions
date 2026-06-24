# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stack = []
        tmp = head

        while tmp:
            stack.append(tmp.val)
            tmp = tmp.next
        
        tmp = head

        while stack:
            tmp.val = stack.pop()
            tmp = tmp.next
        
        return head