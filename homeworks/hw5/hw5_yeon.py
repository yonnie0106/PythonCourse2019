class Node: 
	def __init__(self, _value = None, _next = None):
		self.value = _value
		self.next = _next

	def __str__(self):
		return str(self.value)


class LinkedList():
	def __init__(self, value):   
		self.head = Node(value) ## set value as the head of the list

	def __str__(self): 
		cur = self.head
		while cur is not None:
			print(cur.value, "->", end = ' ')
			cur = cur.next
		print(None)	
		return "" 

	def length(self):
		cur = self.head 
		count = 1 
		while cur.next is not None: 
			cur = cur.next 
			count +=1
		return f"The length of the linked list is {count}."


	def addNode(self, new_value):
		cur = self.head 
		while cur.next is not None: 
			cur = cur.next 
		cur.next = Node(new_value)


	def addNodeAfter(self, new_value, after_node):
		new_node = Node(new_value)
		new_node.next = after_node.next 
		after_node.next = new_node


	def addNodeBefore(self, new_value, before_node):
		cur = self.head
		new_node = Node(new_value)
		while cur.next is not before_node and cur.next is not None:
			cur = cur.next 
		cur.next = new_node
		new_node.next = before_node

	def removeNode(self, node_to_remove):
		cur = self.head
		while cur.next is not None and cur.next is not node_to_remove:
			cur = cur.next
		cur.next = node_to_remove.next

	def removeNodeByValue(self, value): 
		cur = self.head
		previous = None
		find_value = False
		while cur is not None and find_value == False: 
			if cur.value == value:
				previous.next = cur.next
				find_value == True
				cur = cur.next
			else:
				previous = cur
				cur = cur.next 

	def reverse(self):
		cur = self.head
		previous = None
		while cur is not None:
			following = cur.next 
			cur.next = previous
			previous = cur
			cur = following
		self.head = previous
		return self





l = LinkedList(1)
print(l)

l.addNode(2)
l.addNode(3)
l.addNode(4)
print(l)
print(l.length())

l.addNodeAfter(20, l.head.next)
l.addNodeAfter(20,l.head.next)
print(l)

l.addNodeBefore(10,l.head.next)
print(l)

l.removeNode(l.head.next)
print(l)

l.removeNodeByValue(20)
print(l)

l.reverse()
print(l)