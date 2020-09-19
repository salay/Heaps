class Heap:
	# heap class takes in a list 
	# and a comparator function that defines how priority is determined in the heap
	def __init__(self, heapList=[], comparator=None):
		self.heapList = [0] + heapList
		if comparator:
			self.comparator = comparator
		else:
			# comparator defaults to prioritizing the lowest value in the heap
			# therefore constructing a min heap by default
			def findMin(i, j):
				if i <= j:
					return i
				return j
			self.comparator = findMin
		self.buildHeap()
	
	@property
	def heapLength(self):
		return len(self.heapList) - 1
	
	def buildHeap(self):
		i = len(self.heapList) / 2
		while (i > 0):
			self.percDown(i)
			i = i - 1
		return self.heapList

	def percUp(self,i):
		# as long as there is a parent element
		while i/2 > 0:
			# if the value at the current index is higher priority that its parent (value at i/2)
			# then swap the value with its parent (percolate up)
			if self.heapList[i] == self.comparator(self.heapList[i], self.heapList[int(i/2)]):
				self.heapList[int(i/2)], self.heapList[i] = self.heapList[i], self.heapList[int(i/2)]
			# if the current value is not higher priority than the parent, no longer percolate up
			else:
				break
			i = int(i/2)

	def percDown(self, i):
		# as long as there is at least a left child
		while i * 2 < len(self.heapList):
			priorityChild = self.priorityChildIndex(i)
			# compare the value at current index to the higher priority child
			# if the value at the current index is NOT higher priority than the child, 
			# it needs to be swapped with the priority child (percolated down),
			# in order to make sure that each subtree is also a heap (meaning it has the highest priority value at the root)
			if self.heapList[i] != self.comparator(self.heapList[i], self.heapList[priorityChild]):
				self.heapList[i], self.heapList[priorityChild] = self.heapList[priorityChild], self.heapList[i]
			# if the current value is the highest priority between its children, no longer percolate down
			else:
				break
			i = priorityChild

	def priorityChildIndex(self, i):
		# returns the index of the child that is higher priority
		# checks if the right child exists AND if the right child is higher priority than the left
		# if so, then returns the right child
		if (i * 2 + 1) < len(self.heapList) and self.heapList[i * 2 + 1] == self.comparator(self.heapList[i * 2 + 1], self.heapList[i * 2]):
			return i * 2 + 1
		# otherwise the left child is returned
		return i * 2

	def insert(self,k):
		self.heapList.append(k)
		self.percUp(self.heapLength)

	def heapPop(self):
		popped = self.heapList[1]
		self.heapList[1] = self.heapList[len(self.heapList) - 1]
		self.heapList.pop()
		if self.heapLength > 0:
			self.percDown(1)
		return popped

import heapq
import unittest
class TestHeaps(unittest.TestCase):
	def test_heap_min(self):
		python_heap = [2,7,4,1,8,1]
		my_heap = Heap(heapList=[2,7,4,1,8,1])
		heapq.heapify(python_heap)
		self.assertEqual(my_heap.heapList, [0] + python_heap)

		python_heap2 = [7,6,7,6,9]
		my_heap2 = Heap(heapList=[7,6,7,6,9])
		heapq.heapify(python_heap2)
		self.assertEqual(my_heap2.heapList, [0] + python_heap2)

		python_heap3 = [2, 2, 8, 8, 4, 4]
		my_heap3 = Heap(heapList=[2, 2, 8, 8, 4, 4])
		heapq.heapify(python_heap3)
		self.assertEqual(my_heap3.heapList, [0] + python_heap3)

	def test_heap_max(self):
		def findMax(i, j):
			if i >= j:
				return i
			return j
		python_heap = [2,7,4,1,8,1]
		my_heap = Heap(heapList=[2,7,4,1,8,1], comparator=findMax)
		heapq._heapify_max(python_heap)
		self.assertEqual(my_heap.heapList, [0] + python_heap)

		python_heap2 = [7,6,7,6,9]
		my_heap2 = Heap(heapList=[7,6,7,6,9], comparator=findMax)
		heapq._heapify_max(python_heap2)
		self.assertEqual(my_heap2.heapList, [0] + python_heap2)

		python_heap3 = [2, 2, 8, 8, 4, 4]
		my_heap3 = Heap(heapList=[2, 2, 8, 8, 4, 4], comparator=findMax)
		heapq._heapify_max(python_heap3)
		self.assertEqual(my_heap3.heapList, [0] + python_heap3)

if __name__ == '__main__':
	unittest.main()