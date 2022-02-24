import math

"""
determine if the sum of two integers is equal to the given value

seperately, find for index values
"""
arr = [5, 1, 4, 2, 1, 5]
target = 10
def two_sum_set(arr, target):
    mySet = set()
    for i in arr:
        if target - i in mySet:
            return True
        mySet.add(i)
    return False

#print(two_sum_set(arr, target))

#have values as keys, and indexes as values.
def two_sum_dict(arr, target):
    myDict = {}
    for i in range(len(arr)):
        if target - arr[i] in myDict:
            return [myDict[target - arr[i]], i]
        myDict[arr[i]] = i
    return []
print(two_sum_dict(arr, target))

arr2 = [1, 3, 4, 5, 6]
def missing_sum(arr):
    n = len(arr) + 1
    my_sum = (n * (n+1))/2
    arr_sum = sum(arr)
    return int(my_sum - arr_sum)

print(missing_sum(arr2))

arr3 = [1, 4, 9, 25, 36]

def missing_sum_sq(arr):
    n = len(arr) + 1
    my_sum = (n * (n + 1) * ((2 * n) + 1)) / 6
    arr_sum = sum(arr)
    return int(math.sqrt(my_sum - arr_sum))
print(missing_sum_sq(arr3))

myDict = [{"User": "Ruti", "Age": 24, "email": "abcabc@gmail.com"},
{"User": "Mom", "Age": 12, "email": "blahblah@gmail.com"}, 
{"User": "Dad", "Age": 17, "email": ""}]

for i in range(len(myDict)):
    if myDict[i]["email"] != "":
        print(myDict[i]["email"])