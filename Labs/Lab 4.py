#Kristen Tse
#Data Structures
#6/21/19
#Lab 4: Review

#Coding Problems

#Problem 5
#a) O(n^2)
#b)
import random
def random_str(n):
    letters = "abcdefghijklmnopqrstuvwxyz"
    lst = []
    for i in range(1, n+1):
        lst.append(random.choice(letters))
    lst = " ".join(lst)
    return lst


#Problem 6
def powers(base, n):
    prev_num = 1
    for i in range(1, n+1):
        prev_num *= base
        yield prev_num


#Problem 7
def is_palindrome(input_str, low, high):
    if (low == high) or ((low+1) == high):
        return True
    else:
        if input_str[low] == input_str[high]:
            return is_palindrome(input_str, low+1, high-1)
        return False


#Problem 8
def partition(lst):
    pivot = lst[0]
    i = 1
    j = len(lst)-1
    while i < j:
        while lst[i] < pivot:
            i += 1
        while lst[j] > pivot and i < j:
            j -= 1
        if lst[i] > pivot and lst[j] < pivot:
            lst[i], lst[j] = lst[j], lst[i]
    if lst[i] > pivot:
        lst[0], lst[i-1] = lst[i-1], lst[0]
    else:
        lst[0], lst[i] = lst[i], lst[0]
    return lst
