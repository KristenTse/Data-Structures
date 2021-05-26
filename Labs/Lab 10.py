#Kristen Tse
#Data Structures
#8/9/19
#Lab 10


#Problem 2: List Intersection
#This function should run in O(n) average time. The operations in the first loop consist
#of setting an item into the dictionary, which costs O(1) each case and O(n) for the
#whole loop. The second loop consists of appending to the intersections list, which also
#costs O(1) each case and O(n) for the whole loop. In total that is O(2n) = O(n).
#The worst-case running time should be also be O(n) as well.
def list_intersection(lst1, lst2):
    dict = {}
    intersections = []
    
    for i in range(max(len(lst1), len(lst2))):
        if len(lst1) > len(lst2):
            dict[lst1[i]] = None
        else:
            dict[lst2[i]] = None
    for i in range(min(len(lst1), len(lst2))):
        if len(lst1) > len(lst2) and lst2[i] in dict:
            dict[lst2[i]] = True
        elif len(lst1) <= len(lst2) and lst1[i] in dict:
            dict[lst1[i]] = True
    return [key for key, val in dict.items() if val == True]


#Problem 3: Find Mode
#Worst-case running time is O(n)
#I don't think there is a way to improve the running time, as O(n) using a dictionary is
#fairly efficient
def mode_of_list(lst):
    dict_nums = {}
    for num in lst:
        if num in dict_nums:
            dict_nums[num] += 1
        else:
            dict_nums[num] = 1
            
    curr_mode = None
    for key, val in dict_nums.items():
        if curr_mode is None:
            curr_mode = key
        elif val > dict_nums[curr_mode]:
            curr_mode = key
    return curr_mode

            
#Problem 4: Two Sum on Unsorted List
def two_sum(lst, target):
    dict_nums = {}
    for pos in range(len(lst)):
        complement = target - lst[pos]
        if lst[pos] not in dict_nums:
            dict_nums[lst[pos]] = pos
        if complement in dict_nums:
            return (dict_nums[complement],dict_nums[lst[pos]])
    return (None, None)

    
#Problem 5: Anagrams
def is_anagram(str1, str2):
    dict_str = {}
    if len(str1) != len(str2):
        return False
    
    for char in str1:
        if char in dict_str:
            dict_str[char] += 1
        else:
            dict_str[char] = 1
    for char in str2:
        if char in dict_str:
            dict_str[char] -= 1
        else:
            return False
    for key, val in dict_str.items():
        if val != 0:
            return False
    return True         