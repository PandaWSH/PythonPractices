#Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        sentinel = ListNode(1) #create the sentinel, value doesn't matter
        c = sentinel

        while l1 and l2:    
            if l1.val > l2.val:
                c.next = l2
                l2 = l2.next
            else:
                c.next = l1
                l1 = l1.next
            c = c.next # doesn't affect sentinuel.rest
        # 后面的两个while l1和while l2写复杂了，用method 2即可
        while l2:
            c.next = l2
            l2 = l2.next
            c = c.next

        while l1:
            c.next = l1
            l1 = l1.next
            c = c.next
        return sentinel.next

    # second time - 第二轮自己写也用了这个方法
    def mergeTwoList2(self, l1, l2):
        dummy = cur = ListNode(0)#same
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        # -----------above part is the same

        cur.next = l1 or l2 # IMPORTANT ：此时l1和l2必定已经有一个为None，这一行目的在于append上还没变None的LList剩下的部分
        cur = cur.next # if delet this uneccessary line, it improve from 81% & 77% --> 93% & 98%
        return dummy.next

        ''' explain why that uneccessary line
        --------------this is very important ----------
        after assign sentinel to c, they were linked:
        c.rest = xxx would change sentinel.rest
        However, while assign c = c.next, it doesn't affect the "rest" part of sentinel.
        Thus, when final return sentinel.rest, it's always the changing "rest" part that we want

        To further explain:
        --------------
        a = [1,2]
        b = a
        b[0] = 3 #partial change, DOES affect
        a
        >> [3,2]
        --------------
        a = [1,2]
        b = a
        b = [3,4]
        a
        >> [1,2] #specific entire change (or understood as variabled re-definition), NO affect
        ---------------
        a = [1,2]
        b = a
        b = b + [3] #similar to previous one
        a
        >> [1,2]
        '''
