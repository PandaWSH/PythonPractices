# Implement a stack
# --------------------
# Problem statement: 
# Check if its empty
# Push a new item
# Pop an item
# Peek at the top item
# Return the size
# ---------------------

class Stack(object):
	
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return len(self) == 0

	def pushNew(item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	# return the top element but not removing
	def peek(self):
		return self.items[len(self.items) - 1]

	# return the size of the stack
	def size(self):
		return len(self) 

