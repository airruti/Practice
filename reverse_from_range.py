arr = [1, 2, 3, 4, 5, 6]
arr2 = [[0, 1], [2, 3], [1, 5]]

def swap(arr, start, end):
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start =+ 1
        end -= 1

for i in range(len(arr2)):
    swap(arr, arr2[i][0], arr2[i][1])


dic = {}

