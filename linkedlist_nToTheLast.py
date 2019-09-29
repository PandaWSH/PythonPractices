# --------------------
# Linked List Reversal
# --------------------

# Logistic I:
class Node(object):
	def __init__(self, value):
		self.value = value
		self.next = None

def nth(n, head):
	# initialize
	leftpoint = head
	rightpoint = head

	for i in range(n-1):

		# edge case
		if not rightpoint.next:
			raise LookupError("edge case")

		# if not edge case
		rightpoint = rightpoint.next

	# after moved n noded from the head, and there's still value
	while rightpoint.next:
		# keep n nodes section, move 2 pointers together
		# stop when the right pointer hits the ending edge
		leftpoint = leftpoint.next
		rightpoint = rightpoint.next

	return leftpoint
