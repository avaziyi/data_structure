# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 22:28:09 2013

@author: 子怿
"""

class Stack:
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def clear(self):
		del self.items[:]

	def empty(self):
		return self.size() == 0

	def size(self):
		return len(self.items)

	def top(self):
		return self.items[self.size()-1]


def divideBy2(decNumber):
	remstack = Stack()

	while decNumber > 0:
		rem = decNumber % 2
		remstack.push(rem)
		decNumber = decNumber // 2

	binString = ""
	while not remstack.empty():
	        binString = binString + str(remstack.pop())

	return binString

if __name__ == '__main__':
    print(divideBy2(233))