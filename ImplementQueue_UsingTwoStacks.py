# Implement a Queue - Using Two Stacks
# Given the Stack class below, implement a Queue class using two stacks!
# Note, this is a "classic" interview problem. 
# Use a Python list data structure as your Stack.

# KEY: pull elements out from a stack -- reverse the order
#      pull elements out from a queue -- order keeps the same

class Queue2Stack(object):
	def __init__(self):
		self.instack = []
		self.outstack = []

	def enqueue(self,element):
		self.instack.append(element)

	def dequeue(self):
		if not self.outstack:
			while self.instack:
				self.outstack.append(self.instack.pop())
				
		return self.outstack.pop()
