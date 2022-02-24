arr = ["un", "iq", "ue"]
charSet = set()

def overlap(charSet, s): #helper function to say if chars we're looking at are already in the set
    prev = set()
    for c in s:
        if c in charSet or c in prev:
            return True
        prev.add(c)
    return False

#backtracking
def backtrack(i):
    if i == len(arr):
        return len(charSet)
    res = 0
    if not overlap(charSet, arr[i]):
        for c in arr[i]:
            charSet.add(c)
        res = backtrack(i + 1)
        for c in arr[i]:
            charSet.remove(c)
    return max(res, backtrack(i+1))

print(backtrack(0))

# index 0
"""
charSet = ()
overlap(charSet, "un"):
    prev = set()
    for c in "un":
        if c in charSet or c in prev:
            return True
        prev.add(c) #always adding each char to the prev() set so 1. u not in either, add to prev. 2. n not in either, add to prev. prev has 'u' and 'n'
    return False #if it goes through all the words and no matching was found, returns false.

backtrack(0):
    if 0 == len(arr):
        return len(charSet) #which is 0, charSet starts empty
    result = 0
    if not overlap(charSet, "un"): # this results in False. this will execute
        for c in "un":
            charSet.add(c) #adds each to charSet. now charSet has "u and n"
        res = backtrack(i + 1) recursive call to backtrack
"""


