#a collection of array problems 

arr = [1, 2, 3]
arr2 = ["a", "b", "c"]
arr3 = [1, 2, 3, 4, -4, -3, -2, -1]


def pairup(arr, arr2):
    arr3  = []
    for i in range(len(arr)):
        arr3.append([arr[i], arr2[i]])
    return arr3

print(pairup(arr,arr2))

def maxelem(arr):
    myMax = 0
    for i in arr:
        if i > myMax:
            myMax = i
    return myMax

print(maxelem(arr))

def reverselist(arr):
    newArr = []
    for i in arr:
         newArr = [i] + newArr
    return newArr

print(reverselist(arr3))

"""
5 =   00000101
25 =  00011001
      00011100  0(1) + 0(2) + 1(4) + 1(8) + 1(16) = 28
"""
arr4 = [25, 10, 2, 8, 5, 3]

def max_XOR(arr):
    maxSum = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            maxSum = max(maxSum, arr[i] ^ arr[j])

    return maxSum

print(max_XOR(arr4))


def reverseWord(string: str) -> str:
    return " ".join(reversed(string.split(" ")))

print(reverseWord("this is a sentence that needs to be reversed"))

def sumNumIndex(nums, target):
    myMap = {}
    for i in range(len(nums)): 
        if target - nums[i] in myMap:
            res = [myMap[target - nums[i]], i]
            return res
        myMap[nums[i]] = i 
        print(myMap)
    return []

print(sumNumIndex([5, 6, 3, 1, 4, 0], 11))

def add_no_arithmetic_ops(a, b):
    while a != 0:
        
        a, b = ((a & b) << 1),  (a ^ b)

    return b

print(add_no_arithmetic_ops(5, 6))

s = "aaaaabaaaa"
def non_repeat(s):
    ch = s[0]
    for i in s:
        if i != ch:
            return i
    return "all the same"

print(non_repeat(s))

this_arr = [1, 1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 10, 11, 11]
def duplicate_nums(arr):
    mySet = set()
    ans = []
    for i in arr:
        if i in mySet:
            ans.append(i)
        mySet.add(i)
    return ans

print(duplicate_nums(this_arr))

def rem_dups(arr):
    i = 1
    while i < len(arr):
        if arr[i] in arr[:i]:
            arr.pop(i)
        else: i += 1
    return arr

print(rem_dups(this_arr))