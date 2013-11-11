# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 22:40:44 2013

@author: 子怿
"""

class Queue:
	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.append(item)

	def dequeue(self):
		return self.items.pop(0)

	def empty(self):
		return self.size() == 0

	def size(self):
		return len(self.items)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print queue.size()
print type(queue)
queue.empty()
print queue.size()