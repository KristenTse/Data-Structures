import ArrayQueue

class LinkedBinaryTree:
    class Node:
        # Binary Tree nodes store a single data element, and a reference to their left child and right child
        # It is also helpful to keep track of the parent of a Node
        # The parent of a node v is the node u for which v is either the left child or right child
        # That is, if u.left is v or u.right is v, then v.parent is u (and vice-versa)
        def __init__(self, data, left=None, right=None):
            # Set the data, left, and right values
            self.data = data
            self.parent = None
            self.left = left
            self.right = right
            # As described above, if self.left is a node (not None), then its parent is self: we set self.left.parent = self
            if self.left is not None:
                self.left.parent = self
            # We do the same for self.right. If it is a node, set its parent to `self`
            if self.right is not None:
                self.right.parent = self

    def __init__(self, root=None):
        # Create a new LinkedBinaryTree with the given Node as the root. Compute and store the size (number of nodes)
        self.root = root
        self.size = self.subtree_count(self.root)

    # Returns number of nodes in the subtree rooted by `subtree_root`
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

    # Returns the sum of all the (data values of the) nodes in the subtree rooted by `subtree_root`
    def subtree_sum(self, subtree_root):
        if subtree_root is None:
            return 0
        left_sum = self.subtree_sum(subtree_root.left)
        right_sum = self.subtree_sum(subtree_root.right)

        return left_sum + right_sum + subtree_root.data

    def height(self):
        return self.subtree_height(self.root)

    # Returns the height of the subtree rooted by `subtree_root`
    # Recall the height is the max length of any path (= number of EDGES on the path)
    #   from the root (i.e., `subtree_root`) to a leaf node.
    # Important to note: The length of the path from `subtree_root` to either of its children is 1
    #   (a child is connected directly to its parent by a single edge)
    def subtree_height(self, subtree_root):
        if subtree_root.left is None and subtree_root.right is None:
            return 0
        elif subtree_root.left is None:
            # right is not None (but left is)
            return 1 + self.subtree_height(subtree_root.right)
        elif subtree_root.right is None:
            # left is not None (but right is)
            return 1 + self.subtree_height(subtree_root.left)
        else:
            # left and right are both not None
            left_height = self.subtree_height(subtree_root.left)
            right_height = self.subtree_height(subtree_root.right)

            return 1 + max(left_height, right_height)


    ### The following are several different ways to traverse the nodes of a tree
    ### preorder, inorder, postorder work by traversing the subtrees rooted by the current node's children recursively
    ###   We also yield the current node.
    ### preorder yields the current node before recursing on the left, then right subtrees (the subtrees rooted by the left and right child, respectively)
    ### inorder recurses on the right subtree, then yields the current node, then recurses on the right subtree
    ### postorder recurses on the left, then right subtrees, and yields the current node after recursing.
    ### Remember it this way: when do we yield the current node? pre = BEFORE recursing. in = IN-between recursive calls. post = AFTER recursing.

    # preorder traversal
    def preorder(self):
        yield from self.subtree_preorder(self.root)

    # yields all values in the nodes of the subtree
    # rooted at "subtree_root" in preorder
    def subtree_preorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield subtree_root.data
            yield from self.subtree_preorder(subtree_root.left)
            yield from self.subtree_preorder(subtree_root.right)

    # postorder traversal
    def postorder(self):
        yield from self.subtree_postorder(self.root)

    # yields all values in the nodes of the subtree
    # rooted at "subtree_root" in postorder
    def subtree_postorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield from self.subtree_postorder(subtree_root.left)
            yield from self.subtree_postorder(subtree_root.right)
            yield subtree_root.data

    # inorder traversal
    def inorder(self):
        yield from self.subtree_inorder(self.root)

    # yields all values in the nodes of the subtree
    # rooted at "subtree_root" in inorder
    def subtree_inorder(self, subtree_root):
        if subtree_root is None:
            return
        else:
            yield from self.subtree_inorder(subtree_root.left)
            yield subtree_root.data
            yield from self.subtree_inorder(subtree_root.right)


    ## The last way to "traverse" the tree is rather different.
    ## Sometimes called "level order", it yields all the nodes in level 0, then all the nodes in level 1, then level 2, ... (and so on)
    ## It is sometimes also referred to by the name of the method used to accomplish this "level order" traversal: "breadth-first" search
    ## It uses a queue!
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

    # We will define our iterator to use the breadth-first ("in-order") method of traversing the tree
    def __iter__(self):
        for node in self.breadth_first():
            yield node.data
