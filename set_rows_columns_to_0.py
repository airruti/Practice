################set rows and columns to 0################

arr2 = [[1 for i in range(6)] for j in range(7)]

arr2[2][4] = 0
arr2[2][2] = 0
arr2[4][1] = 0

rows = len(arr2)
columns = len(arr2[0])

row_set = set()
column_set= set()

for i in range(rows):
    for j in range(columns):
        if arr2[i][j] == 0:
            row_set.add(i)
            column_set.add(j)

for i in range(rows):
    for j in range(columns):
        if (i in row_set or j in column_set):
            arr2[i][j] = 0

print(arr2)