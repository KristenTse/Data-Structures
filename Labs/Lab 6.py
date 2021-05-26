#Kristen Tse
#Data Structures
#7/5/19
#Lab 6


#Problem 1
class ArrayDeque:
    INITIAL_CAPACITY = 8
    
    def __init__(self):
        #Initialize an empty Deque
        self.data = [None] * ArrayDeque.INITIAL_CAPACITY
        self.num_of_elems = 0
        self.front_ind = None
        self.back_ind = None

    def __len__(self):
        #Return number of elements in the Deque
        return self.num_of_elems
    
    def is_empty(self):
        #Returns True if Deque is empty
        return len(self) == 0
    
    def first(self):
        #Returns(without removing) the element at the front of the Deque
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.data[self.front_ind]

    def last(self):
        #Returns (without removing) the element at the back of the Deque
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.data[self.back_ind]

    def enqueue_first(self, elem):
        #Adds elem to the front of the Deque
        if self.num_of_elems == len(self.data):
            self.resize(2* len(self.data))
        if self.is_empty():
            self.data[0] = elem
            self.front_ind = 0
            self.back_ind = 0
            self.num_of_elems += 1
        else:
            self.data[self.front_ind - 1] = elem
            self.front_ind = (self.front_ind - 1) % len(self.data)
            self.num_of_elems += 1
                            

    def enqueue_last(self, elem):
        #Adds elem to the back of the Deque
        if self.num_of_elems == len(self.data):
            self.resize(2* len(self.data))
        if self.is_empty():
            self.data[0] = elem
            self.front_ind = 0
            self.back_ind = 0
            self.num_of_elems += 1
        else:
            end = (self.front_ind + self.num_of_elems) % len(self.data)
            self.data[end] = elem
            self.back_ind += 1
            self.num_of_elems += 1

    def dequeue_first(self):
        #Remove and return the element at the front of the Deque
        if self.is_empty():
            raise Exception("Deque is empty")
        else:
            elem = self.data[self.front_ind]
            self.data[self.front_ind] = None
            self.front_ind += 1
            self.num_of_elems -= 1
            return elem

    def dequeue_last(self):
        #Remove and return the element at the back of the Deque
        if self.is_empty():
            raise Exception("Deque is empty")
        else:
            elem = self.data[self.back_ind]
            self.data[self.back_ind] = None
            self.back_ind = (self.back_ind - 1) % len(self.data)
            self.num_of_elems -= 1
            return elem

    def resize(self, new_capacity):
        old_data = self.data
        self.data = [None] * new_capacity
        old_front = self.front_ind
        old_back = self.back_ind
        for new_ind in range(self.num_of_elems):
            self.data[new_ind] = old_data[old_front]
            old_front = (old_front + 1) % len(old_data)
        self.front_ind = 0
        self.back_ind = self.num_of_elems - 1


#Problem 2
class ArrayStack:
    def __init__(self):
        self.data = []
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return (len(self) == 0)
    def push(self, item):
        self.data.append(item)
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data.pop()
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data[-1]
    
def balanced_expression(str_input):
    stack = ArrayStack()
    left = ['(', '[', '{']
    right = [')', ']', '}']
    parentheses = list(str_input)
    for char in parentheses:
        if char in left:
            stack.push(char)
        elif char in right:
            ind = right.index(char)
            if stack.is_empty():
                return False
            if stack.top() == left[ind]:
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False
    
    
#Problem 3
def get_tags(html_str):
    start_ind = html_str.find("<")
    end_ind = html_str.find(">", start_ind)
    while start_ind != -1:
        yield html_str[start_ind:end_ind+1]
        start_ind = html_str.find("<", end_ind+1)
        end_ind = html_str.find(">", start_ind)

def is_matched_html(html_str):
    stack = ArrayStack()
    for tag in get_tags(html_str):
        if tag[1] != "/":
            stack.push(tag)
        else:
            if stack.top()[1:] == tag[2:]:
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False