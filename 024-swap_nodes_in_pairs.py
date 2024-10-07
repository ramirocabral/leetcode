# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        act = head
        aux = head.next
        prev = None

        while act and act.next:
            sig = act.next
            if prev != None : prev.next = sig

            act.next = sig.next
            sig.next = act
            prev = act
            act = act.next
        
        if aux :return aux
        return head
