# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head and head.next:
            next_next_node = head.next.next
            new_head = head.next
            new_head.next = head
            head.next = next_next_node
        else:
            return head
        
        previous_node = head
        current_node = head.next
        while current_node and current_node.next:
            next_next_node = current_node.next.next
            swap_node = current_node.next
            swap_node.next = current_node
            previous_node.next = swap_node
            previous_node = current_node
            current_node.next = next_next_node
            current_node = next_next_node
            

        return new_head