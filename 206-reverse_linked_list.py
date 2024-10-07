# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None):
            return None
        curr = head
        prev = None
        while (curr.next != None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        curr.next = prev

        return curr
