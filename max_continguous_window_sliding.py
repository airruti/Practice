size = 3
arr = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
sum = 16

#fixed window
#max sum of certain size
def fixed(arr, size):
    currentSum = 0
    maxSum = float("-inf")
    for i in range(len(arr)):
        currentSum += arr[i]
        if (i >= size - 1):
            maxSum = max(maxSum, currentSum)
            currentSum -= arr[i - (size - 1)]
    print(maxSum)

fixed(arr, size)

#dynamic window
#smallest subarray a given sum 
def dynamic(arr, sum):
    start = 0
    currentSum = 0
    minArray = float("inf")

    for end in range(len(arr)):
        currentSum += arr[end]
        while currentSum >= sum:
            minArray = min(minArray, end - start + 1)
            currentSum -= arr[start]
            start += 1
    print(minArray)
dynamic(arr, sum)
