"""
File: queue2.py

Circular-Array Queue implementation
"""

from arrays import Array

class CircularArrayQueue(object):
    """ Circular-Array-based queue implementation."""

    DEFAULT_CAPACITY = 10  # Class variable applies to all queues
    
    def __init__(self):
        """Queue constructor"""
        self._items = Array(CircularArrayQueue.DEFAULT_CAPACITY)
        self._front = 0
        self._rear = -1
        self._size = 0

    def enqueue(self, newItem):
        """Adds newItem to the rear of queue."""
        # Resize array if necessary
        if len(self) == len(self._items):
            temp = Array(2 * self._size)
            if self._front < self._rear:
                j = 0
                for i in xrange(self._front, self._rear+1):
                    temp[j] = self._items[i]
                    j += 1
                self._items = temp
            if self._front > self._rear: 
                j = 0
                for i in xrange(self._front, self._size):
                    temp[j] = self._items[i]
                    j += 1   
                for i in xrange(self._rear+1):
                    temp[j] = self._items[i]
                    j += 1
                self._items = temp  
            self._front = 0
            self._rear = self._size-1    
        # newItem goes at logical end of array
        if self._rear == len(self._items) - 1:
            self._rear = 0
        else:    
            self._rear += 1
        self._size += 1
        self._items[self._rear] = newItem            

    def dequeue(self):
        """Removes and returns the item at front of the queue.
        Precondition: the queue is not empty."""
        oldItem = self._items[self._front]
        if self._front == len(self._items) - 1:
            self._front = 0
        else:    
            self._front += 1
        self._size -= 1
        return oldItem

    def peek(self):
        """Returns the item at front of the queue.
        Precondition: the queue is not empty."""
        return self._items[self._front]

    def __len__(self):
        """Returns the number of items in the queue."""
        return self._size

    def isEmpty(self):
        return len(self) == 0

    def __str__(self):
        """Items strung from front to rear."""
        result = ""   
        if self._front < self._rear:
            for i in xrange(self._front, self._rear+1):
                result += str(self._items[i]) + " "
        if self._front > self._rear: 
            for i in xrange(self._front, len(self._items)):
                result += str(self._items[i]) + " " 
            for i in xrange(self._rear+1):
                result += str(self._items[i]) + " "   
        return result


def testQueue():
    queue = CircularArrayQueue()
    while True:
        print "Test Queue Menu:"
        print "1 - Enqueue"
        print "2 - Dequeue"
        print "3 - Peek"
        print "4 - len()"
        print "5 - isEmpty"
        print "6 - str"
        print "7 - exit testing"
        response = raw_input("Choice (1 - 6)? ")
        if response == '1':
            item = raw_input("Enter the new item to enqueue")
            queue.enqueue(item)
        elif response == '2':
            if len(queue) >= 1:
                item = queue.dequeue()
                print "The item dequeued was:",item
            else:
                print "Cannot dequeue from an empty queue!"
        elif response == '3':
            if len(queue) >= 1:
                item = queue.peek()
                print "The fron item in the queue is:",item
            else:
                print "Cannot peek at an empty queue!"
        elif response == '4':
            print "The number of elements in the queue is",len(queue)
        elif response == '5':
            print "queue.isEmpty() ==",queue.isEmpty()
        elif response == '6':
            print "The queueu is:",str(queue)
        elif response == '7':
            break
        else:
            print "Invalid Menu Choice!"         

testQueue()