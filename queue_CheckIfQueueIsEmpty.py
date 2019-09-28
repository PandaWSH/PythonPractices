# --------------------
# Check if Queue is Empty
# Enqueue
# Dequeue
# Return the size of the Queue
# --------------------

# Logistic I:
# class Queue(object):

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return len(self.items) == 0

	def enQueue(self,e): #add to the front
		self.items.insert()

	def deQueue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)