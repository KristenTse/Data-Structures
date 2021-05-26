#Kristen Tse
#Data Structures
#8/2/19
#Lab 9

from BinarySearchTreeMap import BinarySearchTreeMap
from LinkedBinaryTree import LinkedBinaryTree


#Problem 2: Check if two Binary Trees Have the Same Keys
def are_bst_keys_same(bst1, bst2):
    if len(bst1) != len(bst2): #one tree has more keys than the other
        return False
    dict = {}
    for node1 in bst1.inorder():
        dict[node1.item.key] = None
    for node2 in bst2.inorder():
        if node2.item.key not in dict:
            return False
    return True


#Problem 3: Check if Tree is BST
def is_bst(binary_tree):        
    return is_bst_helper(binary_tree.root)[0]

def is_bst_helper(subtree_root):
    if subtree_root is None:
        return (True, None, None)
    else:
        leftbool, leftmin, leftmax = is_bst_helper(subtree_root.left)
        rightbool, rightmin, rightmax = is_bst_helper(subtree_root.right) 
        if leftmin == None and leftmax == None:
            leftmin = subtree_root.data
            leftmax = subtree_root.data
        if rightmin == None and rightmax == None:
            rightmin = subtree_root.data
            rightmax = subtree_root.data
        if (leftbool is True) and (rightbool is True) and (leftmax < subtree_root.data < rightmin):
            res = True
        else:
            res = False
        return (res, leftmin, rightmax)