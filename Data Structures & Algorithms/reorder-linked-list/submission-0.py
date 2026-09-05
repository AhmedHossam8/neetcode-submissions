# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # Getting Length
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        
        # splitting the list into two halves
        mid = (length + 1) // 2
        mid_node = head
        i = 1
        while i < mid:
            mid_node = mid_node.next
            i += 1

        # Reverse the second half
        prev = None
        current = mid_node

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Start merging both
        left = head
        right = prev

        while left and right:
            next_left = left.next
            next_right = right.next

            left.next = right
            right.next = next_left

            right = next_right
            left = next_left