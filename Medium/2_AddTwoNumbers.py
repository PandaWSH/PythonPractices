# Definition for singly-linked list.
# my method: 92ms + 13.3 MB (32.3% + )
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        summ = self.returnNumber(l1) + self.returnNumber(l2)
        summ = str(summ) #convert to string
        summ = [int(a) for a in summ]
        print(summ)

        cur = ListNode(summ[0])
        N = ListNode(summ[0])
        next_n = cur
        i = 1
        while i < len(summ):
            N = ListNode(summ[i])
            N.next = next_n
            next_n = N
            i += 1
        return N
              
    def returnNumber(self,l1):
        number = 0
        tentime = 0
        while l1 != None:
            val = l1.val
            number += val*10**tentime
            tentime +=1
            l1 = l1.next
        return number