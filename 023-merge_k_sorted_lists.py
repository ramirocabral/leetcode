# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists):
        head = ListNode()
        current = head
        while ((min_value := self.get_min(lists)) != 99999):
            current.next = ListNode(min_value)
            current = current.next

        return head.next


    # get the minimum val of the lists
    def get_min(self, lists) -> int:
        list_position = 0
        min = 99999
        list_position = -1
        for position, curr_list in enumerate(lists):
            if (curr_list != None):
                if curr_list.val <= min:
                    list_position = position
                    min = curr_list.val
        if (min != 99999):
            lists[list_position] = lists[list_position].next

        return min
