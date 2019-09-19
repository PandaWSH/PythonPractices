# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
            
            
class Solution(object):
	# Hashtabe (dynamic) 36ms + 18.6MB
    def hasCycle(self, head):
        nodesSeen = set() # a set is a data type that does not accept duplicates
        while head is not None: # when head is None, you've reached end of linkedlist
            if head in nodesSeen:
                return True
            else:
                nodesSeen.add(head)
            head = head.next # move on to next node
        return False

    # used class instead of set, but similar logic to method 1
    def hasCycle(self, head):
    	dic = {}
    	while head:
	        if head in dic:
	            return True
	        dic[head] = 0
	        head = head.next
	    return False

 	# two pointer 32ms + 18.1MB [better] ----------- puzzle ------------
	def hasCycle(self, head):
	    """
	    :type head: ListNode
	    :rtype: bool
	    """
	    #empty List
	    if not head:
	    	return False
	    #create two pointer
	    p,q=head,head

	    while p and q:
	        if p.next:
	        	p=p.next
	        else: 
	        	break
	        if q.next and q.next.next:
	        	q=q.next.next
	        else:
	        	break
	        if p==q:
	        	return True
	    return False

	# two pointer 36ms + 18.2MB
	def hasCycle(self, head):
	    fast = slow = head
	    while fast and fast.next:
	        fast = fast.next.next 
	        slow = slow.next
	        if slow is fast:
	            return True
	    return False