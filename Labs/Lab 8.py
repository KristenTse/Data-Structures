#Kristen Tse
#Data Structures
#7/19/19
#Lab 8


#Problem 2: Circular Shift Linked List
from DoublyLL import DoublyLinkedList

def right_circular_shift(lnk_lst):
    first_node = lnk_lst.header.next
    secondtolast_node = lnk_lst.trailer.prev.prev
    last_node = lnk_lst.trailer.prev
    lnk_lst.header.next = last_node
    lnk_lst.trailer.prev = secondtolast_node
    last_node.prev = lnk_lst.header
    last_node.next = first_node
    first_node.prev = last_node
    secondtolast_node.next = lnk_lst.trailer
    return lnk_lst


#Problem 3: Count Values in Binary Tree
from LinkedBinaryTree import LinkedBinaryTree

def count_val(root, value):
    tree = LinkedBinaryTree(root)
    counter = 0
    for val in tree.subtree_postorder(root):
        if val == value:
            counter += 1
    return counter


#Problem 4: Invert a Binary Tree
def invert_binary_tree(bin_tree):
    def invert_helper(subtree_root, new_root):
        if subtree_root is None:
            return
        else:
            if subtree_root.right is not None:
                new_root.left = LinkedBinaryTree.Node(subtree_root.right.data)
                new_root.left.parent = new_root
                invert_helper(subtree_root.right, new_root.left)
            if subtree_root.left is not None:
                new_root.right = LinkedBinaryTree.Node(subtree_root.left.data)
                new_root.right.parent = new_root
                invert_helper(subtree_root.left, new_root.right)
            return
    new_root = LinkedBinaryTree.Node(bin_tree.root.data)
    invert_helper(bin_tree.root, new_root)
    new_tree = LinkedBinaryTree(new_root)
    return new_tree


#Problem 5: Count Number of Leaves, 1-child, and 2-child Nodes
import ArrayQueue
class LinkedBinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.parent = None
            self.left = left
            self.right = right
            if self.left is not None:
                self.left.parent = self
            if self.right is not None:
                self.right.parent = self

    def __init__(self, root=None):
        self.root = root
        self.size = self.subtree_count(self.root)

    def subtree_count(self, subtree_root):
        if subtree_root is None:
            return 0
        left_count = self.subtree_count(subtree_root.left)
        right_count = self.subtree_count(subtree_root.right)
        return left_count + right_count + 1

    def __len__(self):
        return self.size

    def is_empty(self):
        return len(self) == 0

    def sum_nodes(self):
        return self.subtree_sum(self.root)

    def subtree_sum(self, subtree_root):
        if subtree_root is None:
            return 0
        left_sum = self.subtree_sum(subtree_root.left)
        right_sum = self.subtree_sum(subtree_root.right)
        return left_sum + right_sum + subtree_root.data

    def height(self):
        return self.subtree_height(self.root)

    def subtree_height(self, subtree_root):
        if subtree_root.left is None and subtree_root.right is None:
            return 0
        elif subtree_root.left is None:
            return 1 + self.subtree_height(subtree_root.right)
        elif subtree_root.right is None:
            return 1 + self.subtree_height(subtree_root.left)
        else:
            left_height = self.subtree_height(subtree_root.left)
            right_height = self.subtree_height(subtree_root.right)
            return 1 + max(left_height, right_height)

    def preorder(self):
        yield from self.subtree_preorder(self.root)

    def subtree_preorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield subtree_root.data
            yield from self.subtree_preorder(subtree_root.left)
            yield from self.subtree_preorder(subtree_root.right)

    def postorder(self):
        yield from self.subtree_postorder(self.root)

    def subtree_postorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield from self.subtree_postorder(subtree_root.left)
            yield from self.subtree_postorder(subtree_root.right)
            yield subtree_root.data

    def inorder(self):
        yield from self.subtree_inorder(self.root)

    def subtree_inorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield from self.subtree_inorder(subtree_root.left)
            yield subtree_root.data
            yield from self.subtree_inorder(subtree_root.right)

    def breadth_first(self):
        if self.is_empty():
            return
        node_queue = ArrayQueue.ArrayQueue()
        node_queue.enqueue(self.root)
        while node_queue.is_empty() == False:
            curr_node = node_queue.dequeue()
            yield curr_node.data
            if curr_node.left is not None:
                node_queue.enqueue(curr_node.left)
            if curr_node.right is not None:
                node_queue.enqueue(curr_node.right)

    def __iter__(self):
        for node in self.breadth_first():
            yield node.data


    def subtree_children_dist(self, subtree_root):         
        if subtree_root.left is None and subtree_root.right is None:
            #leaf node
            return [1, 0, 0]
        elif subtree_root.left is not None and subtree_root.right is not None:
            #two children
            lres = self.subtree_children_dist(subtree_root.left)
            rres = self.subtree_children_dist(subtree_root.right)
            return [lres[0]+rres[0], lres[1]+rres[1], lres[2]+rres[2]+1]
            
        elif subtree_root.left is None:
            #has right child
            res = self.subtree_children_dist(subtree_root.right)
            return [res[0], res[1]+1, res[2]]

        elif subtree_root.right is None:
            #has left child
            res = self.subtree_children_dist(subtree_root.left)
            return [res[0], res[1]+1, res[2]]