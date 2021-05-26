#Kristen Tse
#Data Structures
#5/31/19
#Lab 1


#Problem 1
#Write a fucntion that takes an array A and a number S and finds if there are three
#numbers in A that sum to S

def sumthree(lst, targetsum):
    for i in lst:
        for j in lst:
            for k in lst:
                if i + j + k == targetsum:
                    return i, j, k

print(sumthree([1,2,4,6,9], 5))


#Problem 2
#Write a function that accepts as parameters an array A and a nuber S and finds if there
#is a continuous subarray of A that sums to S

def sumcont(lst, targetsum):
    for start in range(len(lst)):
        for stop in range(start+1, len(lst)+1):
            sum = 0
            for num in lst[start:stop]:
                sum += num
            if sum == targetsum:
                return lst[start:stop]
            
print(sumcont([3,1,7,-2,4], 6)) 

    
#Review on Classes
class Person:
    def __init__(self, fname, lname, age):
        self.firstname = fname
        self.lastname = lname
        self.age = age
    def changename(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def havebirthday(self):
        self.age += 1
    def __str__(self):
        return (self.firstname + " " + self.lastname + " is " + str(self.age) + " years old")

nathan = Person("Nathaniel", "Grammel", 25)
print(nathan)
print(str(nathan))


#Problem 3
#Write a function that takes two sorted arrays and merges them into one sorted array.
#Don't use the sort method
#***COULD SHOW UP ON FUTURE INTERVIEWS

def merge(lst1, lst2):
    #input:[1,3,5,6], [1,2,3,4,7]
    #output: [1,1,2]
    
    result = []
    ind1 = 0
    ind2 = 0
    while ind1 < len(lst1) and ind2 < len(lst2):
        if lst1[ind1] <= lst2[ind2]:
            result.append(lst1[ind1])
            ind1 += 1
        else:
            result.append(lst2[ind2])
            ind2 += 1

    while ind1 < len(lst1):
        result.append(lst1[ind1])
        ind1 += 1

    while ind2 < len(lst2):
        result.append(lst2[ind2])
        ind2 += 1
    return result
           
print(merge([1,3,5,6],[1,2,3,4,7]))


#Problem 4
#Give a sorted array and a number, find the number in the array and return the index of
#the number in the array, or return -1 if the number is not in the array. (You may
#assume the array is sorted.

def search(lst, targetnum):
    if targetnum < lst[0] or targetnum > lst[-1]: #for efficiency; not necessary
        return -1
    for pos in range(len(lst)):
        if lst[pos] == targetnum:
            return pos
        if lst[pos] > targetnum: #also for efficiency
            return -1
    return -1


def search2(lst, targetnum): #binary search
    start = 0
    end = len(lst)
    while start < end:
        mid = (start+end)//2
        if targetnum == lst[mid]:
            return mid
        elif targetnum < lst[mid]:
            end = mid
        else:
            start = mid