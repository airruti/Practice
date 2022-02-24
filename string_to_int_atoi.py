class Solution:
    def myAtoi(s: str):
        new_s = ""
        num = 0

        for c in s:
            if(s[0]).isalpha():
                return 0
            if c.isnumeric() or c == '-' or c == '.' or c == '+':
                if new_s == '-+' or new_s == '+-':
                    return 0
                if (c == '.'):
                    break
                new_s += c

        if new_s == "":
            return 0

        num = int(new_s)

        if num < (2**31) * -1:
            return (2**31) * -1
        if num > (2**31) - 1:
            return (2**31) - 1

        return num
    print(myAtoi("-932458734534323"))