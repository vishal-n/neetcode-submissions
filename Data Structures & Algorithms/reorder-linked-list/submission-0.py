# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        lst = []
        reordered_lst = []
        tmp = head

        while tmp:
            lst.append(tmp.val)
            tmp = tmp.next
        
        reordered_lst.append(lst[0])
        lst.pop(0)

        while lst:
            if lst:
                curr_ele = lst.pop()
                reordered_lst.append(curr_ele)
            if lst:
                curr_ele = lst.pop(0)
                reordered_lst.append(curr_ele)
        
        tmp = head
        i = 0
        
        while tmp:
            tmp.val = reordered_lst[i]
            i += 1
            tmp = tmp.next





