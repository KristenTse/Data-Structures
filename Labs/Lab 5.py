#Kristen Tse
#Data Structures
#6/28/19
#Lab 5


#Problem 1: Binary Search
#assume sorted list
def binary_search(lst, val, low, high):
    if low == high:
        if lst[low] == val:
            return low
        else:
            return None
    else:
        mid = (low+high)//2
        if lst[mid] >= val:
            return binary_search(lst, val, low, mid)
        else: #lst[mid] < val
            return binary_search(lst, val, mid+1, high)


#Problem 2: Nested Lists Sum
def nested_list_sum(lst):
    if isinstance(lst, int):
        return lst
    elif lst == []:
        return 0
    return nested_list_sum(lst[0]) + nested_list_sum(lst[1:])

        
#Problem 3.1: Selection Sort, Iterative
def find_min(lst, start, end):	
    if start == end:
        return start
    if lst[start] < lst[end]:
        return find_min(lst, start, end-1)
    elif lst[start] > lst[end]:
        return find_min(lst, start+1, end)

def selection_sort(lst):
    for i in range(len(lst)):
        smallest = find_min(lst, i, len(lst)-1)
        if lst[smallest] < lst[i]:
            lst[smallest], lst[i] = lst[i], lst[smallest]
    return lst

        
#Problem 3.2: Selection Sort, Recursion
def selection_sort_recursive(lst, low, high):
    if low == high:
        return lst
    else:
        smallest = find_min(lst, low, high)
        lst[smallest], lst[low] = lst[low], lst[smallest]
        selection_sort_recursive(lst, low+1, high)
        return lst
    

#Problem 4: A New Sorting Algorithm
def partition(lst, start, end):
    pivot = lst[start]
    pivot_ind = start
    i = start+1
    j = end
    while i < j:
        while lst[i] < pivot and i < j:
            i += 1
        while lst[j] > pivot and i < j:
            j -= 1
        if i < j: 
            lst[i], lst[j] = lst[j], lst[i]
    if lst[start] > lst[j]: 
        lst[start], lst[j] = lst[j], lst[start]
        pivot_ind = j
    else:
        lst[i-1], lst[start] = lst[start], lst[i-1]
        pivot_ind = i-1
    return pivot_ind

def quicksort(lst, start, end):
    if start == end or start > end:
        return lst
    else:
        pivot = partition(lst, start, end)
        quicksort(lst, start, pivot-1)
        quicksort(lst, pivot+1, end)
        return lst