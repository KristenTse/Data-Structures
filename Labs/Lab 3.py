#Kristen Tse
#Data Structures
#6/14/19
#Lab 3


#Find First 1, O(log2(n))
def first1(lst):
    left = 0
    right = len(lst)-1
    ind = None
    found = False
    while ((found == False) and (left <= right)):
        mid = (left + right) // 2
        if left == right:
            ind = mid
            found = True
        elif lst[mid] == 0:
            left = mid + 1
        else: #lst[mid] == 1
            right = mid
    return ind


#Compute e, O(n)
def e_approximation(n):
    final = 1
    factorial = 1
    for i in range(1, n):
        factorial *= i
        final += 1/factorial
    return final


#Two-Sum, O(n)
def two_sum(sorted_lst, target):
    i = 0
    j = len(sorted_lst)-1
    while i < j:
        if (sorted_lst[i] + sorted_lst[j]) > target:
            j -= 1
        elif (sorted_lst[i] + sorted_lst[j]) < target:
            i += 1
        else:
            return (i, j)
    return None


#Separate Negatives and Positives, O(n)
def split_neg_pos(lst):
    pos = None
    neg = None
    i = 0
    j = len(lst) - 1
    while i < j:
        while lst[i] < 0:
            i += 1
        pos = lst[i]
        while lst[j] > 0:
            j -= 1
        neg = lst[j]
        if (i < j): 
            lst[i] = neg
            lst[j] = pos
    return lst


#Zeros to End, O(n)
def move_zeros(lst):
    first_zero = -1
    for j in range(len(lst)):
        if lst[j] == 0 and first_zero == -1:
            first_zero = j

        elif lst[j] != 0 and first_zero != -1:
            lst[first_zero] = lst[j]
            lst[j] = 0
            first_zero += 1
    return lst


#Recursion Practice: Min
def find_min(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        small = find_min(lst[1:])
        if lst[0] < small:
            return lst[0]
        else:
            return small


#Test Cases
def main():
    #First1
    print(first1([0,0,0,0,1,1]))

    #Computing e
    print(e_approximation(15))

    #Two-sum
    print(two_sum([-3, -2, 0, 5, 17], 2))

    #Separate Negatives and Positives
    print(split_neg_pos([-7, 5, -3, 10, 5, -9]))

    #Zeros to End
    print(move_zeros([1,0,2,0,0,3,4]))

    #Practice Recursion
    print(find_min([5, -1, 9, 6, 0]))

main()
