
arr = [55, 7, 78, 12, 42]

for j in range(len(arr), 0, -1):
    for i in range(1, j):
        if arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]

print(arr)