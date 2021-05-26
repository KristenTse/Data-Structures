#Kristen Tse
#Data Structures
#7/12/19
#Lab 7


#Problem 1
class DoublyLinkedList:
    class Node:
        def __init__(self, data=None, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next
        def disconnect(self):
            self.data = None
            self.prev = None
            self.next = None
    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0
    def __len__(self):
        return self.size
    def is_empty(self):
        return len(self) == 0
    def first_node(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self.header.next
    def last_node(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self.trailer.prev
    def add_after(self, node, data):
        pred = node
        succ = node.next
        new_node = DoublyLinkedList.Node(data, pred, succ)
        pred.next = new_node
        succ.prev = new_node
        self.size += 1
    def add_first(self, data):
        self.add_after(self.header, data)
    def add_last(self, data):
        self.add_after(self.trailer.prev, data)
    def add_before(self, node, data):
        self.add_after(self.node.prev, data)
    def delete_node(self, node):
        pred = node.prev
        succ = node.next
        pred.next = succ
        succ.prev = pred
        data = node.data
        node.disconnect()
        self.size -= 1
        return data
    def delete_first(self):
        if self.is_empty():
            raise Exception("List is empty")
        self.delete_node(self.first_node())
    def delete_last(self):
        if self.is_empty():
            raise Exception("List is empty")
        self.delete_node(self.last_node())
    def __iter__(self):
        if self.is_empty():
            return
        curr_node = self.first_node()
        while curr_node is not self.trailer:
            yield curr_node.data
            curr_node = curr_node.next
    def __repr__(self):
        return '[' + '<-->'.join(str(item) for item in self) + ']'

    
class LinkedStack:
    def __init__(self):
        self.data = DoublyLinkedList()
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def push(self, elem):
        self.data.add_last(elem)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        elem = self.data.trailer.prev.data
        self.data.delete_last()
        self.size -= 1
        return elem

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data.last_node().data
    


#Problem 2
class ArrayLeakyStack:
    def __init__(self, max_num_of_elems):
        self.max_num_of_elems = max_num_of_elems
        self.data = [None] * self.max_num_of_elems
        self.size = 0
        self.top_ind = -1

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def push(self, elem):
        self.top_ind = (self.top_ind + 1) % self.max_num_of_elems
        self.data[self.top_ind] = elem
        if self.size < self.max_num_of_elems:
            self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        elem = self.data[self.top_ind]
        self.data[self.top_ind] = None
        self.top_ind = (self.top_ind - 1) % self.max_num_of_elems
        self.size -= 1        
        return elem
        
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data[self.top_ind]
    

class LinkedLeakyStack():
    def __init__(self, max_num_of_elems):
        self.max_num_of_elems = max_num_of_elems
        self.size = 0
        self.data = DoublyLinkedList()

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def push(self, elem):
        if self.size < self.max_num_of_elems:
            self.data.add_last(elem)
            self.size += 1 
        else:
            self.data.delete_first()
            self.data.add_last(elem)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        elem = self.data.trailer.prev.data
        self.data.delete_last()
        self.size -= 1
        return elem
        
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data.last_node().data



#Problem 3
class ArrayQueue:
    INITIAL_CAPACITY = 8
    def __init__(self):
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = None
    def __len__(self):
        return self.num_of_elems
    def is_empty(self):
        return len(self) == 0
    def enqueue(self, elem):
        #if the array is full, a resize is done first
        if self.num_of_elems == len(self.data):
            self.resize(2 * len(self.data))
        #if the list was empty before trying to enqueue
        if self.is_empty():
            self.data[0] = elem
            self.front_ind = 0
            self.num_of_elems += 1
        #if there were already items in the array
        else:
            back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
            self.data[back_ind] = elem
            self.num_of_elems += 1
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        elem = self.data[self.front_ind]
        self.data[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        if self.is_empty():
            self.front_ind = None
        elif len(self) < len(self.data) // 4:
            self.resize(len(self.data) // 2)
        return elem
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.front_ind]
    def resize(self, new_capacity):
        old_data = self.data
        self.data = [None] * new_capacity
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front_ind = 0


class QStack:
    def __init__(self):
        self.size = 0
        self.data_queue1 = ArrayQueue()
        self.data_queue2 = ArrayQueue()

    def __len__(self): #O(1) time
        return self.size

    def is_empty(self): #O(1) time
        return len(self) == 0

    def push(self,elem): #O(1) amortized time, O(n) worst case because of the resize
        self.data_queue1.enqueue(elem)
        self.size += 1

    def pop(self): #O(n^2) time because the whole list is enqueued and dequeued
        if self.is_empty():
            raise Exception("Queue is empty")
        for i in range(self.data_queue1.num_of_elems - 1):
            self.data_queue2.enqueue(self.data_queue1.first())
            self.data_queue1.dequeue()
        elem = self.data_queue1.first()
        self.data_queue1.dequeue()
        self.data_queue1, self.data_queue2 = self.data_queue2, self.data_queue1
        return elem

    def top(self): #O(n^2) time because the whole list is enqueued and dequeued; similar to pop()
        if self.is_empty():
            raise Exception("Queue is empty")
        for i in range(self.data_queue1.num_of_elems):
            if self.data_queue1.num_of_elems == 1:
                elem = self.data_queue1.first()
            self.data_queue2.enqueue(self.data_queue1.first())
            self.data_queue1.dequeue()
        self.data_queue1, self.data_queue2 = self.data_queue2, self.data_queue1
        return elem