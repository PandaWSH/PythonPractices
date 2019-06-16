class Solution:
    #my method 84ms, 24.4MS (42.14%+9.35)
    # store all val into a string, then determine whether the sring is palindrome
    # slow and demand space
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        value = []
        cur = head
        while cur!= None and cur.next != None:
            value.append(cur.val)
            cur = cur.next
        value.append(cur.val)
        print(value)
        
        if value == value[::-1]:
            return True
        else:
            return False

    # Above method could be simplified:
    #76ms + 23.8 MB
    def isPalindrome(self, head: 'ListNode') -> 'bool':
        if not head or not head.next:
            return True
        
        s = [head.val, ]
        
        while head.next:
            head = head.next
            s.append(head.val)
                               
        return s[::-1] == 

    # faster method 
    def isPalindrome(self, head: 'ListNode') -> 'bool':
    
        if not head or not head.next : return True

        slow = head
        fast = head.next
        ans = [slow.val]

        while fast.next and fast.next.next :
            fast = fast.next.next
            slow = slow.next
            ans.append(slow.val)

        if not fast.next :
            two = slow.next
        else : 
            two = slow.next.next
        while ans :
            temp = ans.pop()
            if temp != two.val :
                return False
            else :
                two = two.next
        return True
            
        
            
        