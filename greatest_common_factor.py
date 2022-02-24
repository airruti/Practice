#############greatest common factor

"""
find max of the array
set variable to keep track of current number and gcd
from 1 to the max, if both values % current number is 0:
    set gcd = to current number
"""

input = [9, 36]
max = max(input[0], input[1])

def find_gcd(arr):
    num = 1
    gcd = 0
    while num <= max:
        if (arr[0] % num  == 0 and arr[1] % num == 0):
            gcd = num
        num += 1
    return gcd

print(find_gcd(input))