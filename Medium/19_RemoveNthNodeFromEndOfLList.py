# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 36ms + 13MB (88.74% + 94.73%)
    # two pass algorithm
    # get the total length first, then skip the Nth node
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head #to memorized the input head
        length = 0 #initialize the length counter
        first = head
        
        while first != None:
            length += 1
            first = first.next # counter the length of the ListNode
            
        length -= n
        first = dummy
        while length > 0:
            length -= 1
            first = first.next
        #skip the nth node
        first.next = first.next.next
        return dummy.next

    # 36ms + 13.3 (88.74% + 77.60%)
    # one pass algorithm (two pointers)
    #
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head #to memorized the input head
        first = dummy
        second = dummy
        for i in range(n+1):
            first = first.next
        
        while first != None:
            first = first.next
            second = second.next
        
        second.next = second.next.next
        return dummy.next