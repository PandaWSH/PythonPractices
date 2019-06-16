class Solution:
    #iterative method shared online
    # 44ms + 14.3 MB(61.10% + 93.33%)   
    def reverseList(self, head):
        if not head:
            return None
        
        #base condition
        pre = None
        cur = head
        while cur:
            next_n = cur.next
            cur.next = pre
            pre = cur
            cur = next_n
        return pre

    # still confusing
    def reverseList(self,head):
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
