# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    #submission 1 32ms + 13.3MB
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

# submission 3 28ms + 13.2 MB (note method 4)
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        while cur.next != None and cur.next.next != None:
            self.swap2(cur)
            cur = cur.next.next
        return dummy.next
    
    def swap2(self,pre):
        dum = pre.next
        pre.next = dum.next
        dum.next = dum.next.next
        pre.next.next = dum

# submission 4 32ms + 13.3 MB (note method 2)
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:return head
        p,q=head,head.next
        r=q#r是新的头结点
        while p and q:
            k=p#
            p.next=q.next
            q.next=p
            if p.next and p.next.next:
                p=p.next
                q=p.next
                k.next=q
            else:
                break
        return r

# submission 5 28ms + 13.2MB (98.97% + 34.74%)
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:return head
        
        pre = new_h = ListNode(0)
        while head and head.next:
            temp = head.next
            head.next = temp.next
            temp.next = head
            
            pre.next = temp
            pre = head
            head = head.next
        return new_h.next
            
        
    