# --------------------
# Linked List Reversal
# --------------------

# Logistic I:
# 1. scan the list from lsft to the right
# 2. when see a open parenthesis, add to the stack

class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

def reverse(head):
	current = head
	previous = None
	nextnode = None

	while current:
		# KEY: copy current.next before updating them
		# 先记下nextnode值，再改变pointer方向
		nextnode = current.next
		current.next = previous

		# 再把previous和current一起往后挪一个
		previous = current
		current = nextnode

	return previous

