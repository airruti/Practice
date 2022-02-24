s = "this is a test"

def reverseWords(string):
    startindex = 0
    currindex = 0
    string = string[::-1]
    newString = ""

    print(string)


    while currindex < len(string):
        if string[currindex] == " " or currindex == len(string) - 1:
            newString += string[currindex:startindex:-1]
            startindex = currindex - 1
        currindex += 1
    return newString

#"this is a test"
# 0123456789

print(reverseWords(s))
