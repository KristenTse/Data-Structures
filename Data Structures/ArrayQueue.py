class ArrayQueue:
    INITIAL_CAPACITY = 8
    
    def __init__(self):
        # Use a list to store queue elements
        # self.data is the list used to store elements
        # len(self.data) is our capacity (how many elements we can store before resizing
        # self.num_of_elems is the number of elements in the queue
        # self.front_ind will be the index of the "front" of the queue (the first element to have been inserted)
        self.data = [None] * ArrayQueue.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = None

    # O(1) time
    def __len__(self):
        # len(self) is the number of elements in the queue == self.num_of_elems
        return self.num_of_elems

    # O(1) time
    def is_empty(self):
        # Queue is empty if it has no elements (len is 0)
        return len(self) == 0

    # Amortized worst case running time is O(1)
    # But an individual enqueue can take worst case O(n) if resize is done
    # This time complexity is just like the append operation in dynamic arrays
    def enqueue(self, elem):
        # If number of elements == capacity (we've filled the list completely), resize
        if self.num_of_elems == len(self.data):
            self.resize(2 * len(self.data))
            
        # If list was empty before trying to enqueue `elem`,
        # Put it at index 0 at set the front_ind to 0 (since this is the first elem in the queue)
        if self.is_empty():
            self.data[0] = elem
            self.front_ind = 0
            self.num_of_elems += 1
        # Otherwise, if the queue already had elements
        else:
            # back_ind is the index of the "back" of the queue
            # The back is where we will add new elements
            # Using mod (as in % len(self.data)) makes the back "wrap around"
            #       to index 0 if it exceeds len(self.data)
            # Example: [None, None, None, 1];
            #       front_ind == 3, num_of_elems == 1, len(self.data) == 4
            #       Then: back_ind = (3 + 1) % 4 = 0
            # Another Example: [3, None, 1, 2];
            #       front_ind == 2, num_of_elems == 3, len(self.data) == 4
            #       Then: back_ind = (2 + 3) % 4 = 1
            #       1 is at the front of the queue
            #       3 is "last" in the queue, and the new element will be after 3
            #       If the new element is 4, after inserting, the array will be: [3, 4, 1, 2] and 4 is now "last"
            # This is often referred to as a "circular array" because of how we cycle back around to the beginning of the queue
            back_ind = (self.front_ind + self.num_of_elems) % len(self.data)
            self.data[back_ind] = elem
            self.num_of_elems += 1

    # Amortized worst case running time of O(1)
    # But, an individual dequeue might cause a resize with running time O(n)
    # The time complexity is just like pop in dynamic arrays
    def dequeue(self):
        # Raise an exception if the queue is empty (we can't remove from an empty queue!)
        if self.is_empty():
            raise Exception("Queue is empty")
        # Get the elem at the front of the queue
        # Then set the front to None so that it is "reset"
        elem = self.data[self.front_ind]
        self.data[self.front_ind] = None
        # Once we've removed an element from the front, the next element is now the front
        # Once again, the front should cycle back to index 0 ("wrap around"), so we use mod (% len(self.data))
        # Example: [None, None, 1, 2];
        #       front_ind == 2, num_of_elems == 2, len(self.data) == 4
        #       After we dequeue, we get: [None, None, None, 2]; front_ind == 3; and num_of_elems == 1
        # Another Example: [2, None, None, 1];
        #       front_ind == 3, num_of_elems == 2, len(self.data) == 4
        #       After we dequeue, we get [2, None, None, None], front_ind = (3 + 1) % 4 = 0; num_of_elems == 1
        self.front_ind = (self.front_ind + 1) % len(self.data)
        self.num_of_elems -= 1
        # After removing the front, check if queue is empty. There is no "front" in an empty queue
        if self.is_empty():
            self.front_ind = None
        # As with dynamic arrays, we shrink the underlying array (by half) if we are using less than 1/4 of the capacity
        elif len(self) < len(self.data) // 4:
            self.resize(len(self.data) // 2)
        return elem

    # O(1) running time
    def first(self):
        # The first element in the queue is at the "front" index
        # But we raise an error if the queue is empty
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.data[self.front_ind]

    # Resizing takes time O(n) where n is the number of elements in the queue
    def resize(self, new_capacity):
        # Create new array of size new_capacity, and copy elements to new array
        old_data = self.data
        self.data = [None] * new_capacity
        # The "front" of the old array is at front_ind. We will start copying from the front.
        old_ind = self.front_ind
        for new_ind in range(self.num_of_elems):
            # We copy from the old array starting at the front, to index 0 in the new array
            # In the new array, the "front" will be at index 0
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        # Update the front -- it is now at index 0
        self.front_ind = 0




def insert_sorted(sortedq, elem):
    inserted = False
    for i in range(len(sortedq)):
        first = sortedq.first()
        if first >= elem and inserted == False:
            sortedq.enqueue(elem)
            inserted = True
        val = sortedq.dequeue()
        sortedq.enqueue(val)
    if inserted == False:
        q.enqueue(elem)
    return(sortedq.data)
