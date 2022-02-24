def longestCommonPrefix(strs):
        
    """
    First we take the smallest string from the list of strings and iterate to the length if that smallest string.
    Now we store the each character of first string iteratively in the variable named p.
    After that, We checked that if that variable p is at the index in all strings as it is in first string.
    if it is then we concatenate it to our ans variable, else we return ans variable.
    """
        
    ans = ""
    for i in range(len(min(strs))):
        p = strs[0][i]
        if all(x[i]==p for x in strs):
            ans += p
        else:
            return ans
    return ans    

print(longestCommonPrefix(["", ""]))