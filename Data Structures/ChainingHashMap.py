from DoublyLL import DoublyLinkedList
import random

class ChainingHashMap:
    class Item:
        def __init__(self, key, value):
            self.key = key
            self.value = value
    ## END of Item class

    def __init__(self, N=64, p=40206835204840513073):
        self.table_size = N # N ==> size of hash table (number of "buckets")
        # BAD: self.table = [DoublyLinkedList()] * self.table_size
        self.table = [DoublyLinkedList() for i in range(self.table_size)]
        self.number_of_items = 0
        # Constants for the MAD (Multiply-Add-Divide) compression function:
        #    h(k) = ((a*k + b) mod p) mod table_size
        self.p = p
        self.a = random.randrange(1, self.p-1)
        self.b = random.randrange(0, self.p-1)

    def hash_function(self, key):
        # Using MAD compression method
        #    h(k) = ((a*k + b) mod p) mod table_size
        return ((self.a * hash(key) + self.b) % self.p)  % self.table_size

    def __len__(self):
        return self.number_of_items

    def is_empty(self):
        return len(self) == 0

    def __getitem__(self, key):
        idx = self.hash_function(key)
        bucket = self.table[idx]
        item_node = self.find_item_node(key, bucket)

        if item_node is not None:
            return item_node.data.value
        else:
            raise KeyError("Key", str(key), "is not in the map")


    def find_item_node(self, key, bucket):
        # Returns the node containing the item with key "key"
        # Returns None if the key is not in the bucket
        if bucket.is_empty():
            return None
        
        curr_node = bucket.first_node()
        while curr_node is not bucket.trailer:
            if curr_node.data.key == key:
                return curr_node
            curr_node = curr_node.next
        return None

    def __setitem__(self, key, value):
        idx = self.hash_function(key)
        bucket = self.table[idx]
        item_node = self.find_item_node(key, bucket)

        if item_node is not None:
            item_node.data.value = value
        else:
            new_item = ChainingHashMap.Item(key, value)
            bucket.add_last(new_item)
            self.number_of_items += 1
        
        if self.number_of_items >= self.table_size:
            self.rehash(2 * self.table_size)
        

    def __delitem__(self, key):
        idx = hash_function(key)
        bucket = self.table[idx]

        item_node = self.find_item_node(key, bucket)
        if item_node is not None:
            bucket.delete_node(item_node)
        else:
            raise KeyError(str(key), "is not in the map")

    def __iter__(self):
        for curr_llist in self.table:
            for curr_item in curr_llist:
                yield curr_item.key

    def rehash(self, new_size):
        old_table = self.table
        self.table_size = new_size
        self.table = [DoublyLinkedList() for i in range(self.table_size)]

        for bucket in old_table:
            for item in bucket:
                new_idx = self.hash_function(item.key)
                new_bucket = self.table[new_idx]
                new_bucket.add_last(item)
