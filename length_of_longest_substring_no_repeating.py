################Length of longest substring no repeating characters################
def longestSub(s):
    maxVal = 0
    lastIndex = {}
    startIndex = 0
        
    for i in range(len(s)):
        if s[i] in lastIndex:
            startIndex = max(startIndex, lastIndex[s[i]] + 1)
        maxVal = max(maxVal, i-startIndex + 1)
        lastIndex[s[i]] = i
    return maxVal
print(longestSub("asbsddhsdfkdflfauiefsdf"))