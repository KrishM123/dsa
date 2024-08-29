# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head and head.next):
            new_head = self.helperFunction(head, head.next)
            head.next = None
            return new_head
        else:
            return head

    def helperFunction(self, head, next_head):
        to_ret = None
        if (next_head.next):
            to_ret = self.helperFunction(next_head, next_head.next)

        next_head.next = head
        if to_ret:
            return to_ret
        else:
            return next_head