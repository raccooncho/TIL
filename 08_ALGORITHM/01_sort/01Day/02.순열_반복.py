N = 3
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if j == i:
            continue
        for k in range(1, N + 1):
            if k == i or k == j:
                continue
            print(i, j, k)








