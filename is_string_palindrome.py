############determine if a string is a palindrome

input = "abcdecba"
input2 = 10540501
input3 = "racecar"

input2 = str(input2)

def is_palindrome_odd(someString):
    start = 0
    end = len(someString) - 1
    while someString[start] == someString[end]:
        if (someString[start] != someString[end]):
            return False
        if(start == end):
            return True
        start += 1
        end -= 1
    return False

def is_palindrome_even(someString):
    start = 0
    end = len(someString) - 1
    middle = len(someString) / 2
    while someString[start] == someString[end]:
        if (someString[start] != someString[end]):
            return False
        if(start == middle - 1 and end == middle):
            return True
        start += 1
        end -= 1
    return False


if (len(input3)) % 2 == 0:
    print(is_palindrome_even(input3))
else:
    print(is_palindrome_odd(input3))
