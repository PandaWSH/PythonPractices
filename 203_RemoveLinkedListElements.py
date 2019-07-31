# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#second time
class Solution:
    #my method (72ms + 16.3MB, 91.98% + 80.32%)
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return []
        pointer = head
        while pointer.next != None and pointer != None:
            if pointer.next.val == val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
        # 关键在于，第一位val要放到最后来处理
        if head and head.val == val:
            head = head.next
        return head