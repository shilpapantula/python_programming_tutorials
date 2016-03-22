class stack_using_list:
	"""
	implementing stack using lists in python
	top of the stack is the end of the list
	"""
	def __init__(self):
		self.stack = []
	
	def push(self, item):
		self.stack.append(item)

	def pop(self):
		return self.stack.pop()

	def is_empty(self):
		return self.stack == []

	def peek(self):
		return self.stack[-1]

	def size(self):
		return len(self.stack)

test_stack = stack_using_list()
print test_stack.is_empty()

test_stack.push(1)
print test_stack.peek()

test_stack.push(9)
test_stack.push(5)

print test_stack.size()
print test_stack.pop()
